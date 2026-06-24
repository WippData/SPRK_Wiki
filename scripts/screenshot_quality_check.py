#!/usr/bin/env python3
"""Deterministic screenshot quality checks for SPRK wiki assets.

This intentionally avoids OCR and visual guesswork. The main quality gate is:
if a screenshot includes macOS traffic-light controls from the SPRK app window,
those controls must be cropped close to the top-left edge. Inset window controls
mean the screenshot still contains outer/background context, such as Codex.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

try:
    from PIL import Image
except ImportError:  # pragma: no cover - exercised only on missing dependency
    print("Pillow is required: python3 -m pip install Pillow", file=sys.stderr)
    raise SystemExit(2)


DEFAULT_EDGE_TOLERANCE = 28
EDGE_SAMPLE_PX = 32
TRAFFIC_LIGHT_SEARCH_HEIGHT = 260


@dataclass(frozen=True)
class Bounds:
    left: int
    top: int
    right: int
    bottom: int

    @property
    def width(self) -> int:
        return self.right - self.left

    @property
    def height(self) -> int:
        return self.bottom - self.top


@dataclass(frozen=True)
class TrafficLightCluster:
    red_x: float
    red_y: float
    yellow_x: float
    yellow_y: float
    green_x: float
    green_y: float
    suggested_crop_left: int
    suggested_crop_top: int

    @property
    def edge_offset(self) -> float:
        return max(self.red_x, self.red_y)


@dataclass(frozen=True)
class ScreenshotIssue:
    path: str
    code: str
    severity: str
    message: str
    details: dict


@dataclass(frozen=True)
class EdgeStats:
    edge: str
    sampled_pixels: int
    neutral_dark_ratio: float
    navy_dark_ratio: float
    white_ratio: float


@dataclass
class Component:
    area: int
    bounds: Bounds
    center_x: float
    center_y: float


def png_files(paths: Iterable[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_dir():
            files.extend(sorted(path.rglob("*.png")))
        elif path.suffix.lower() == ".png":
            files.append(path)
    return sorted(dict.fromkeys(files))


def connected_components(mask: list[list[bool]]) -> list[Component]:
    height = len(mask)
    width = len(mask[0]) if height else 0
    seen = [[False for _ in range(width)] for _ in range(height)]
    components: list[Component] = []

    for start_y in range(height):
        for start_x in range(width):
            if seen[start_y][start_x] or not mask[start_y][start_x]:
                continue

            stack = [(start_x, start_y)]
            seen[start_y][start_x] = True
            area = 0
            sum_x = 0
            sum_y = 0
            min_x = max_x = start_x
            min_y = max_y = start_y

            while stack:
                x, y = stack.pop()
                area += 1
                sum_x += x
                sum_y += y
                min_x = min(min_x, x)
                max_x = max(max_x, x)
                min_y = min(min_y, y)
                max_y = max(max_y, y)

                for next_y in range(max(0, y - 1), min(height, y + 2)):
                    for next_x in range(max(0, x - 1), min(width, x + 2)):
                        if seen[next_y][next_x] or not mask[next_y][next_x]:
                            continue
                        seen[next_y][next_x] = True
                        stack.append((next_x, next_y))

            components.append(
                Component(
                    area=area,
                    bounds=Bounds(min_x, min_y, max_x + 1, max_y + 1),
                    center_x=sum_x / area,
                    center_y=sum_y / area,
                )
            )

    return components


def plausible_dot(component: Component) -> bool:
    return (
        15 <= component.area <= 250
        and 4 <= component.bounds.width <= 25
        and 4 <= component.bounds.height <= 25
    )


def color_masks(image: Image.Image) -> tuple[list[list[bool]], list[list[bool]], list[list[bool]]]:
    rgb = image.convert("RGB")
    width, height = rgb.size
    pixels = rgb.load()
    red_mask: list[list[bool]] = []
    yellow_mask: list[list[bool]] = []
    green_mask: list[list[bool]] = []

    for y in range(height):
        red_row: list[bool] = []
        yellow_row: list[bool] = []
        green_row: list[bool] = []
        for x in range(width):
            red, green, blue = pixels[x, y]
            red_row.append(red > 180 and 40 < green < 145 and blue < 145 and red - green > 65)
            yellow_row.append(red > 185 and 120 < green < 225 and blue < 130 and red - blue > 85)
            green_row.append(red < 135 and green > 125 and blue < 150 and green - red > 35)
        red_mask.append(red_row)
        yellow_mask.append(yellow_row)
        green_mask.append(green_row)

    return red_mask, yellow_mask, green_mask


def find_traffic_light_clusters(image: Image.Image) -> list[TrafficLightCluster]:
    width, height = image.size
    image = image.crop((0, 0, width, min(height, TRAFFIC_LIGHT_SEARCH_HEIGHT)))
    red_mask, yellow_mask, green_mask = color_masks(image)
    reds = [component for component in connected_components(red_mask) if plausible_dot(component)]
    yellows = [component for component in connected_components(yellow_mask) if plausible_dot(component)]
    greens = [component for component in connected_components(green_mask) if plausible_dot(component)]

    clusters: list[TrafficLightCluster] = []
    for red in reds:
        for yellow in yellows:
            if not (12 <= yellow.center_x - red.center_x <= 26):
                continue
            if abs(yellow.center_y - red.center_y) > 6:
                continue
            for green in greens:
                if not (28 <= green.center_x - red.center_x <= 52):
                    continue
                if abs(green.center_y - red.center_y) > 6:
                    continue

                clusters.append(
                    TrafficLightCluster(
                        red_x=red.center_x,
                        red_y=red.center_y,
                        yellow_x=yellow.center_x,
                        yellow_y=yellow.center_y,
                        green_x=green.center_x,
                        green_y=green.center_y,
                        suggested_crop_left=max(0, round(red.center_x - 14)),
                        suggested_crop_top=max(0, round(red.center_y - 14)),
                    )
                )

    return sorted(clusters, key=lambda cluster: cluster.edge_offset)


def edge_samples(image: Image.Image) -> list[tuple[str, list[tuple[int, int, int]]]]:
    rgb = image.convert("RGB")
    width, height = rgb.size
    pixels = rgb.load()
    sample = max(1, min(EDGE_SAMPLE_PX, width // 5 if width >= 5 else width, height // 5 if height >= 5 else height))

    left = [pixels[x, y] for y in range(height) for x in range(sample)]
    right = [pixels[x, y] for y in range(height) for x in range(width - sample, width)]
    top = [pixels[x, y] for y in range(sample) for x in range(width)]
    bottom = [pixels[x, y] for y in range(height - sample, height) for x in range(width)]
    return [("left", left), ("right", right), ("top", top), ("bottom", bottom)]


def edge_stats(image: Image.Image) -> list[EdgeStats]:
    stats: list[EdgeStats] = []
    for edge, samples in edge_samples(image):
        neutral_dark = 0
        navy_dark = 0
        white = 0
        for red, green, blue in samples:
            luminance = 0.2126 * red + 0.7152 * green + 0.0722 * blue
            if luminance > 220:
                white += 1
            if luminance < 80 and abs(red - green) < 8 and abs(green - blue) < 8:
                neutral_dark += 1
            if luminance < 80 and blue - red > 10 and blue - green > 0:
                navy_dark += 1

        total = len(samples)
        stats.append(
            EdgeStats(
                edge=edge,
                sampled_pixels=total,
                neutral_dark_ratio=neutral_dark / total,
                navy_dark_ratio=navy_dark / total,
                white_ratio=white / total,
            )
        )
    return stats


def looks_like_external_dark_gutter(stat: EdgeStats) -> bool:
    """Detect neutral dark app/background gutters without flagging SPRK navy UI."""

    return (
        stat.neutral_dark_ratio >= 0.82
        and stat.navy_dark_ratio <= 0.18
        and stat.white_ratio <= 0.20
    )


def check_screenshot(path: Path, edge_tolerance: int) -> list[ScreenshotIssue]:
    issues: list[ScreenshotIssue] = []
    try:
        with Image.open(path) as image:
            width, height = image.size
            clusters = find_traffic_light_clusters(image)
            stats = edge_stats(image)
    except Exception as exc:  # noqa: BLE001 - report any image decode failure
        return [
            ScreenshotIssue(
                path=str(path),
                code="image_decode_failed",
                severity="error",
                message=f"Could not open screenshot: {exc}",
                details={},
            )
        ]

    has_edge_window_controls = any(
        cluster.red_x <= edge_tolerance and cluster.red_y <= edge_tolerance for cluster in clusters
    )

    for cluster in clusters:
        if cluster.red_x <= edge_tolerance and cluster.red_y <= edge_tolerance:
            continue

        issues.append(
            ScreenshotIssue(
                path=str(path),
                code="window_controls_not_edge_cropped",
                severity="error",
                message=(
                    "macOS app window controls are inset from the image edge; "
                    "the screenshot likely includes Codex, desktop, or another background window."
                ),
                details={
                    "image_width": width,
                    "image_height": height,
                    "red_control_center": [round(cluster.red_x, 1), round(cluster.red_y, 1)],
                    "edge_tolerance": edge_tolerance,
                    "suggested_crop_origin": [
                        cluster.suggested_crop_left,
                        cluster.suggested_crop_top,
                    ],
                },
            )
        )

    for stat in stats:
        # Cropped subsets often include an app title bar, and app modals can dim
        # the sidebar into neutral dark pixels. Treat edge gutters as failures
        # only for left/right neutral borders when no edge-cropped app window is
        # visible. The inset-window-control rule catches high-confidence cases.
        if stat.edge not in {"left", "right"}:
            continue
        if has_edge_window_controls:
            continue
        if not looks_like_external_dark_gutter(stat):
            continue

        issues.append(
            ScreenshotIssue(
                path=str(path),
                code="neutral_dark_background_gutter",
                severity="error",
                message=(
                    f"{stat.edge} edge is dominated by neutral dark pixels; "
                    "this looks like Codex, desktop, or another non-app background."
                ),
                details={
                    "edge": stat.edge,
                    "sampled_pixels": stat.sampled_pixels,
                    "neutral_dark_ratio": round(stat.neutral_dark_ratio, 3),
                    "navy_dark_ratio": round(stat.navy_dark_ratio, 3),
                    "white_ratio": round(stat.white_ratio, 3),
                },
            )
        )

    return issues


def print_text_report(files: list[Path], issues: list[ScreenshotIssue]) -> None:
    if not issues:
        print(f"PASS: checked {len(files)} PNG screenshot(s)")
        return

    print(f"FAIL: checked {len(files)} PNG screenshot(s), found {len(issues)} issue(s)")
    for issue in issues:
        print(f"- {issue.path}: {issue.code}")
        print(f"  {issue.message}")
        if issue.details:
            print(f"  details: {json.dumps(issue.details, sort_keys=True)}")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Check SPRK wiki screenshots for deterministic crop-quality issues."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        default=[Path("screenshots/v1-validation")],
        help="PNG files or directories to check. Defaults to screenshots/v1-validation.",
    )
    parser.add_argument(
        "--edge-tolerance",
        type=int,
        default=DEFAULT_EDGE_TOLERANCE,
        help=f"Maximum allowed traffic-light control offset from top-left edge. Default: {DEFAULT_EDGE_TOLERANCE}.",
    )
    parser.add_argument(
        "--format",
        choices=("text", "json"),
        default="text",
        help="Output format. Default: text.",
    )
    args = parser.parse_args(argv)

    files = png_files(args.paths)
    if not files:
        print("No PNG screenshots found.", file=sys.stderr)
        return 2

    issues: list[ScreenshotIssue] = []
    for file in files:
        issues.extend(check_screenshot(file, args.edge_tolerance))

    if args.format == "json":
        print(json.dumps({"checked": len(files), "issues": [asdict(issue) for issue in issues]}, indent=2))
    else:
        print_text_report(files, issues)

    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
