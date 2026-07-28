# @campus-nav/graph

JS/TS pathfinding package — consumes the graph JSON produced by the Python pipeline and runs A* in the browser for instant client-side routing.

## Planned exports
- `loadGraph(url)` — fetch and parse graph.json
- `findPath(graph, fromId, toId)` — A* shortest path, returns ordered node array
- `getNodeById(graph, id)` — lookup room metadata
