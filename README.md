# campus-nav-3d

> 3D campus navigation platform — pilot: Christ University, Kengeri Campus, Bengaluru.
> Scales to tech parks, hospitals, and large multi-building campuses.

## Vision
A self-hostable, embeddable 3D navigation system where users search for rooms, get visual paths through buildings across floors, with a kiosk mode for physical touchscreen deployment and a future QR/AR walking mode.

## Pilot
**Christ University — Kengeri Campus, Bengaluru**
- Source data: PDF floor plans (processed via `pdfplumber` + `shapely`)
- Mode: Kiosk / web search-and-highlight
- Target: Working demo deployable at campus entrance

## Monorepo Structure
```
campus-nav-3d/
├── apps/
│   ├── web/          # Next.js — main 3D nav experience
│   └── admin/        # Floor plan uploader + room tagger
├── packages/
│   ├── engine/       # Three.js scene, camera, path rendering
│   └── graph/        # Nav graph builder + Dijkstra/A* pathfinding
├── services/
│   └── api/          # FastAPI — route computation, data serving
└── data/
    └── christ-kengeri/
        ├── raw/      # Original PDF floor plans (gitignored if sensitive)
        ├── processed/# Extracted GeoJSON room polygons
        └── graph/    # Navigation graph JSON
```

## Tech Stack
| Layer | Tech |
|---|---|
| 3D Rendering | Three.js + React Three Fiber |
| Frontend | Next.js + TypeScript + Tailwind |
| Backend | FastAPI (Python) |
| Database | Supabase (PostgreSQL) |
| PDF Processing | pdfplumber + shapely + ezdxf |
| Pathfinding | Custom A* on room graph |
| Deployment | Vercel (web) + Railway/Render (api) |

## Phases
- **Phase 1 (MVP)**: Static 3D scene + search + path highlight — Kiosk mode
- **Phase 2**: QR-code positioning → walk-me-there mode
- **Phase 3**: Multi-campus SaaS — admin uploads floor plans, gets embed widget

## Status
🟡 In active development

## Co-builders
- [M S Rishav Subhin](https://github.com/msrishav-28)
