from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="campus-nav-3d API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "online", "project": "campus-nav-3d"}

@app.get("/api/campuses")
def list_campuses():
    """List all available campuses."""
    return {"campuses": [{"id": "christ-kengeri", "name": "Christ University — Kengeri Campus", "city": "Bengaluru"}]}

@app.get("/api/campuses/{campus_id}/buildings")
def list_buildings(campus_id: str):
    """List buildings for a campus."""
    return {"campus_id": campus_id, "buildings": []}

@app.get("/api/campuses/{campus_id}/route")
def get_route(campus_id: str, from_room: str, to_room: str):
    """Compute shortest path between two rooms."""
    return {"from": from_room, "to": to_room, "path": [], "status": "graph not loaded yet"}
