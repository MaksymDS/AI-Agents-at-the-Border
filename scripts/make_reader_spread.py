#!/usr/bin/env python3
"""Place consecutive book pages side by side for on-screen spread review.

This is intentionally *not* printer imposition: page 1 stays beside page 2,
page 3 beside page 4, and so on.  It creates a landscape reader's proof while
leaving the portrait, print-ready source PDF untouched.
"""

from __future__ import annotations

import argparse
import logging
from pathlib import Path

from pypdf import PdfReader, PdfWriter, Transformation
from pypdf._page import PageObject


# Quarto/Pandoc output can contain harmless duplicated /Group entries from
# layered SVG artwork.  The reader accepts them; do not turn that known input
# quirk into a wall of warnings every time the release proof is regenerated.
logging.getLogger("pypdf").setLevel(logging.ERROR)


def page_size(page: PageObject) -> tuple[float, float]:
    """Return the visible PDF page dimensions in PostScript points."""
    return float(page.mediabox.width), float(page.mediabox.height)


def add_page_to_spread(spread: PageObject, page: PageObject, x_offset: float) -> None:
    """Merge one original page at its left or right position in a spread."""
    spread.merge_transformed_page(page, Transformation().translate(tx=x_offset, ty=0))


def build_spreads(source: Path, destination: Path) -> tuple[int, int]:
    reader = PdfReader(str(source))
    if not reader.pages:
        raise ValueError(f"{source} contains no pages")

    width, height = page_size(reader.pages[0])
    for number, page in enumerate(reader.pages, start=1):
        if page_size(page) != (width, height):
            raise ValueError(
                f"page {number} is {page_size(page)}, but page 1 is {(width, height)}; "
                "reader spreads require a uniform page size"
            )

    writer = PdfWriter()
    metadata = {
        key: value
        for key, value in (reader.metadata or {}).items()
        if isinstance(key, str) and isinstance(value, str)
    }
    title = metadata.get("/Title", source.stem)
    metadata["/Title"] = f"{title} — Reader spreads"
    writer.add_metadata(metadata)

    for left_index in range(0, len(reader.pages), 2):
        spread = PageObject.create_blank_page(width=width * 2, height=height)
        add_page_to_spread(spread, reader.pages[left_index], 0)
        if left_index + 1 < len(reader.pages):
            add_page_to_spread(spread, reader.pages[left_index + 1], width)
        writer.add_page(spread)

    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("wb") as output:
        writer.write(output)

    return len(reader.pages), len(writer.pages)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a landscape PDF with two sequential book pages per spread."
    )
    parser.add_argument("source", type=Path, help="portrait source PDF")
    parser.add_argument("destination", type=Path, help="landscape reader-spread PDF")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_pages, spreads = build_spreads(args.source, args.destination)
    print(f"Created {args.destination}: {input_pages} book pages on {spreads} reader spreads.")


if __name__ == "__main__":
    main()
