# Web App (Next.js)

Main user-facing 3D navigation experience.

## Pages
- `/` — Campus overview, building selector
- `/campus/[id]` — 3D scene with search + path highlight
- `/kiosk/[id]` — Fullscreen kiosk mode (no header/footer, touch optimized)

## Key components
- `<Scene />` — R3F canvas, loads engine
- `<SearchBar />` — Autocomplete room search
- `<FloorSelector />` — Floor switcher overlay
- `<PathOverlay />` — Animated path tube
