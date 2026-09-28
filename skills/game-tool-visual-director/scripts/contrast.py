"""Contrast ratio for two opaque sRGB hex colors; not a full accessibility audit.

Original implementation of the W3C WCAG 2.2 relative-luminance definition:
https://www.w3.org/TR/WCAG22/#dfn-relative-luminance
"""
import argparse
import json
import re


def rgb(value):
    if not re.fullmatch(r"#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?", value):
        raise ValueError("Use opaque sRGB #RGB or #RRGGBB. Resolve transparency and other color spaces first.")
    digits = value[1:]
    if len(digits) == 3:
        digits = "".join(c * 2 for c in digits)
    return tuple(int(digits[i:i + 2], 16) / 255 for i in (0, 2, 4))


def luminance(value):
    linear = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in rgb(value)]
    return sum(c * weight for c, weight in zip(linear, (0.2126, 0.7152, 0.0722)))


def measure(foreground, background):
    lower, upper = sorted((luminance(foreground), luminance(background)))
    ratio = (upper + 0.05) / (lower + 0.05)
    return {"foreground": foreground, "background": background, "ratio": ratio,
            "threshold_matches": {"4.5:1": ratio >= 4.5, "3:1": ratio >= 3, "7:1": ratio >= 7},
            "scope": "Two opaque sRGB colors only; choose the applicable criterion and inspect actual rendered readability."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("foreground")
    parser.add_argument("background")
    args = parser.parse_args()
    try:
        print(json.dumps(measure(args.foreground, args.background), indent=2))
    except ValueError as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
