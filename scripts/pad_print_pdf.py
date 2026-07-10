#!/usr/bin/env python3
"""Pad a book PDF to a print-signature multiple without moving its back cover.

Blank pages are inserted immediately before the final page, which is the
designed back cover in this project.  This preserves the last-page cover while
making the physical PDF page count a multiple of the requested signature size.
"""

from __future__ import annotations

import argparse
import logging
import os
import tempfile
from pathlib import Path

from pypdf import PdfReader, PdfWriter


logging.getLogger("pypdf").setLevel(logging.ERROR)


def pad_before_back_cover(pdf_path: Path, multiple: int) -> tuple[int, int]:
    reader = PdfReader(str(pdf_path))
    page_count = len(reader.pages)
    if page_count < 2:
        raise ValueError("a book PDF must contain content and a final back cover")
    missing = (-page_count) % multiple
    if missing == 0:
        return page_count, 0

    width = float(reader.pages[-1].mediabox.width)
    height = float(reader.pages[-1].mediabox.height)
    writer = PdfWriter(clone_from=str(pdf_path))
    back_cover_index = len(writer.pages) - 1
    for _ in range(missing):
        writer.insert_blank_page(width=width, height=height, index=back_cover_index)
        back_cover_index += 1

    with tempfile.NamedTemporaryFile(
        suffix=".pdf", prefix=f"{pdf_path.stem}-padded-", dir=pdf_path.parent, delete=False
    ) as temporary:
        temporary_path = Path(temporary.name)
        writer.write(temporary)
    os.replace(temporary_path, pdf_path)
    return page_count + missing, missing


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Pad a book PDF before its final back cover to a signature multiple."
    )
    parser.add_argument("pdf", type=Path, help="book PDF to update in place")
    parser.add_argument("--multiple", type=int, default=4, help="required page multiple (default: 4)")
    args = parser.parse_args()
    if args.multiple < 2:
        parser.error("--multiple must be at least 2")
    total, inserted = pad_before_back_cover(args.pdf, args.multiple)
    print(f"Print signature: {total} pages ({inserted} blank page(s) inserted before the back cover).")


if __name__ == "__main__":
    main()
