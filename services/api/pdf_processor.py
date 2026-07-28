"""PDF floor plan processor — extracts room polygons from scanned/vector PDFs."""
import pdfplumber
import json
from shapely.geometry import Polygon
from pathlib import Path


def extract_rooms_from_pdf(pdf_path: str, floor_number: int = 0) -> dict:
    """
    Extract rectangular room outlines from a vector PDF floor plan.
    Returns GeoJSON-like structure of rooms.

    For scanned PDFs: use OCR layer (pytesseract) separately to label rooms.
    For vector PDFs: room outlines appear as rect/line elements.
    """
    rooms = []
    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[floor_number]
        rects = page.rects
        for i, rect in enumerate(rects):
            x0, y0, x1, y1 = rect['x0'], rect['y0'], rect['x1'], rect['y1']
            width = x1 - x0
            height = y1 - y0
            # Filter noise — real rooms are larger than 20x20 pts
            if width > 20 and height > 20:
                rooms.append({
                    "id": f"room_{floor_number}_{i}",
                    "floor": floor_number,
                    "label": "",  # To be tagged via admin panel
                    "bbox": [x0, y0, x1, y1],
                    "polygon": [
                        [x0, y0], [x1, y0], [x1, y1], [x0, y1], [x0, y0]
                    ]
                })
    return {
        "floor": floor_number,
        "source": str(pdf_path),
        "room_count": len(rooms),
        "rooms": rooms
    }


if __name__ == "__main__":
    import sys
    result = extract_rooms_from_pdf(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 0)
    out = Path("data/christ-kengeri/processed") / f"floor_{result['floor']}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2))
    print(f"Extracted {result['room_count']} rooms → {out}")
