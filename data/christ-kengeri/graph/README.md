# Christ University Kengeri — Navigation Graph

This directory will contain the processed navigation graph once floor plans are ingested.

## Expected files
- `graph.json` — NetworkX node-link format graph of all rooms + connections
- `metadata.json` — building list, floor count, room count

## How to generate
```bash
cd services/api
python pdf_processor.py ../../data/christ-kengeri/raw/block_a_floor_0.pdf 0
python pdf_processor.py ../../data/christ-kengeri/raw/block_a_floor_1.pdf 1
python graph_builder.py  # reads processed/ → writes graph/graph.json
```
