# Handoff: Module 15 — Graphs I: Traversal

Build `15-graphs-1/`. Read `CONVENTIONS.md` and the master spec
first. You own ONLY this folder.

Audience: completed modules 01–14 (DFS/BFS on trees; hash maps;
queues). Trees were graphs with training wheels — say so.

Graph convention (pin it): adjacency list as dict/Map from node →
list of neighbors; nodes are ints or strings; edge lists as pairs.
Grids: `grid[row][col]`, 4-directional moves via a DIRS constant.

## LESSON.md outline
1. Why this exists: anything with relationships — roads, links,
   dependencies, friendships — is a graph. Traversal answers "what
   can I reach, and how fast?".
2. Representations. REQUIRED diagram: the same 5-node graph drawn as
   a picture, its adjacency LIST, and its adjacency MATRIX side by
   side. Cost comparison table (space, edge lookup, iterate
   neighbors).
3. A grid IS a graph: cells are nodes, adjacent cells are edges
   (no need to materialize it). This mental move unlocks half of
   LeetCode.
4. DFS (recursive + iterative) and BFS (queue). The ONE rule that
   differs from trees: a VISITED set, because graphs have cycles.
5. REQUIRED diagram: BFS wavefront on a grid (rings of distance 1,
   2, 3 from a source).
6. How to recognize it: "shortest path, unweighted" → BFS (and ONLY
   BFS); "any path / all reachable / count regions" → DFS or BFS;
   "spreads simultaneously from several places" → multi-source BFS.
7. Worked example: islands count traced (visit, sink, count).
8. Gotchas: forgetting visited (infinite loops), marking visited on
   ENQUEUE not dequeue (the classic BFS dupe bug — diagram or
   spell it out), recursion depth on big grids.

## Exercises (exactly 7)
- ex01 "graph-repr" — `to_adjacency(n, edges, directed)` build the
  dict/Map; `degrees(adj)`; `matrix_to_list(matrix)` and back.
- ex02 "dfs-bfs-basics" — `reachable(adj, start)` → set (DFS,
  iterative or recursive); `bfs_order(adj, start)` → visit order
  (tie-break: neighbors in given order); `connected_components(adj)`
  → count; `path_exists(adj, a, b)`.
- ex03 "island-count" — `count_islands(grid)` and
  `max_island_area(grid)` on 0/1 grids. Efficiency test: 300×300
  grid (forces visited discipline; iterative or careful recursion).
- ex04 "flood-fill-regions" — `flood_fill(image, r, c, color)`;
  `capture_regions(board)` (surrounded-regions shape: border-
  connected cells survive — the "invert the question" insight goes
  in the docstring).
- ex05 "infection-spread" — multi-source BFS: `minutes_to_infect(
  grid)` (rotting-oranges shape as server-malware spread: −1 if
  unreachable healthy servers remain) and `shortest_exit(maze,
  start)` (shortest path length in a 0/1 maze, BFS distance).
- ex06 "clone-graph" — `clone_graph(node)` deep copy via hash map
  old→new (node class with neighbors list provided in the file);
  tests verify structure equality AND full node-identity
  separation.
- ex07 "bipartite-check" — `is_bipartite(adj)` via BFS 2-coloring;
  docstring frames it as "can we split users into two teams with no
  same-team edge". Includes disconnected-graph test (the trap).

## Checkpoint
"Social graph": from a friendship edge list —
`friend_circles(edges, n)` (components), `degrees_of_separation(
edges, a, b)` (BFS distance, −1 if unconnected),
`suggested_friends(edges, user)` (friends-of-friends minus friends,
sorted), `can_two_team(edges, n)` (bipartite). Efficiency test:
50_000 edges.

## SUMMARY.md
Cheat-sheet: representation table, DFS vs BFS decision table
("shortest unweighted → BFS" in bold), visited-on-enqueue rule,
grid-as-graph recipe with DIRS constant, multi-source recipe (seed
the queue with all sources). Mindmap. Self-quiz 8 Qs.
Pattern-recognition drill: 8 one-liners (shortest/spread/regions
cues; a weighted-shortest decoy flagged "module 16").
