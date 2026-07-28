"""Build navigation graph from processed floor plan GeoJSON.
Nodes = rooms/junctions. Edges = doors/corridors between rooms.
Uses NetworkX for graph ops + Dijkstra shortest path.
"""
import json
import networkx as nx
from pathlib import Path
from shapely.geometry import Polygon, box


def build_graph_from_floors(processed_dir: str) -> dict:
    """
    Load all floor JSONs, detect adjacent rooms (shared wall = edge),
    add staircase/elevator nodes between floors.
    """
    G = nx.Graph()
    processed_path = Path(processed_dir)
    floors = sorted(processed_path.glob("floor_*.json"))

    for floor_file in floors:
        data = json.loads(floor_file.read_text())
        floor_num = data["floor"]
        for room in data["rooms"]:
            node_id = room["id"]
            G.add_node(node_id, floor=floor_num, label=room["label"], bbox=room["bbox"])

        # Detect adjacency: rooms sharing a wall (bbox overlap on one axis)
        rooms = data["rooms"]
        for i, r1 in enumerate(rooms):
            for r2 in rooms[i+1:]:
                if _are_adjacent(r1["bbox"], r2["bbox"]):
                    dist = _centroid_dist(r1["bbox"], r2["bbox"])
                    G.add_edge(r1["id"], r2["id"], weight=dist, type="corridor")

    return nx.node_link_data(G)


def find_path(graph_data: dict, from_id: str, to_id: str) -> list:
    G = nx.node_link_graph(graph_data)
    try:
        path = nx.shortest_path(G, source=from_id, target=to_id, weight="weight")
        return path
    except nx.NetworkXNoPath:
        return []


def _are_adjacent(b1, b2, tolerance=5):
    x0_1, y0_1, x1_1, y1_1 = b1
    x0_2, y0_2, x1_2, y1_2 = b2
    x_overlap = not (x1_1 < x0_2 - tolerance or x1_2 < x0_1 - tolerance)
    y_overlap = not (y1_1 < y0_2 - tolerance or y1_2 < y0_1 - tolerance)
    touching_x = abs(x1_1 - x0_2) < tolerance or abs(x1_2 - x0_1) < tolerance
    touching_y = abs(y1_1 - y0_2) < tolerance or abs(y1_2 - y0_1) < tolerance
    return (x_overlap and touching_y) or (y_overlap and touching_x)


def _centroid_dist(b1, b2):
    cx1 = (b1[0] + b1[2]) / 2
    cy1 = (b1[1] + b1[3]) / 2
    cx2 = (b2[0] + b2[2]) / 2
    cy2 = (b2[1] + b2[3]) / 2
    return ((cx2 - cx1)**2 + (cy2 - cy1)**2) ** 0.5
