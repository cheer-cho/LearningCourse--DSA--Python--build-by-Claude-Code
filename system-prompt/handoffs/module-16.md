# Handoff: Module 16 — Graphs II: Ordering, Union-Find & Weighted Paths

Build `16-graphs-2/`. Read `CONVENTIONS.md` and the master spec
first. You own ONLY this folder.

Audience: completed modules 01–15 (traversal fluency assumed; heaps
from module 12 power Dijkstra/Prim).

Language note: Python may use `heapq` here. TypeScript exercises
needing a heap include a small PROVIDED `MinHeap` (marked "provided —
do not edit") inside the exercise file.

Within-module imports: ex04 (Kruskal) SHOULD import `UnionFind` from
ex02's file — building on your own structure is the point.

## LESSON.md outline
1. Why this exists: three questions traversal can't answer — what
   ORDER must dependent tasks run in? are these merged into one
   group as edges arrive? what's the CHEAPEST path when edges have
   weights?
2. Topological sort: only on DAGs. Kahn's algorithm (in-degrees +
   queue) step by step. REQUIRED diagram: small course-prereq DAG
   with in-degrees, two valid orders listed. Cycle = no valid order
   → detection for free (processed count < n).
3. Union-find: near-O(1) "same group?" under merging. Parent forest,
   path compression, union by rank. REQUIRED diagram: forest before/
   after a path-compressed find.
4. MST in plain words (cheapest way to connect everything):
   Kruskal = sort edges + union-find skip-cycles; Prim = grow with
   a heap. When each shines (edge list vs dense/adjacency).
5. Dijkstra: BFS's weighted upgrade — a priority queue always
   expands the cheapest frontier. Worked example: 5-node weighted
   graph traced in a table (dist array evolving). Why negative
   edges break it (one honest paragraph) → Bellman-Ford-style
   relaxation as the fallback, k-rounds variant.
6. How to recognize it: "prerequisites/build order" → topo;
   "groups/merging/redundant connection" → union-find; "connect all
   cheapest" → MST; "shortest with weights" → Dijkstra; "at most k
   hops" → k-round relaxation.
7. Gotchas: topo on cyclic input, forgetting path compression (TLE),
   Dijkstra with stale heap entries (lazy skip pattern), directed
   vs undirected mixups.

## Exercises (exactly 7)
- ex01 "topo-sort" — `build_order(n, prereqs)` → any valid order or
  None/null on cycle (Kahn's); `can_finish(n, prereqs)` → bool.
  Tests validate order by checking constraints, not one fixed
  answer. Efficiency test: 50_000 nodes chain.
- ex02 "build-union-find" — BUILD `UnionFind(n)`: `find` (path
  compression), `union` (by rank/size, returns whether merged),
  `connected`, `component_count`. Efficiency test: 200_000 mixed
  ops (punishes no-compression).
- ex03 "redundant-link" — `redundant_connection(edges)` → the edge
  that closes the first cycle; `count_provinces(matrix)` (adjacency
  matrix → component count via UF; docstring: DFS works too —
  compare).
- ex04 "kruskal-mst" — `min_connection_cost(n, weighted_edges)` →
  total MST cost (or None/null if disconnected) via sort + the
  student's UnionFind (import from ex02). Tests include
  disconnected and duplicate-weight cases.
- ex05 "prim-connect-points" — `min_cost_connect_points(points)`:
  Manhattan-distance complete graph, Prim with a heap (docstring:
  why Kruskal is worse when edges = n²/2).
- ex06 "dijkstra-delivery" — `delivery_times(n, edges, source)` →
  dist map (network-delay shape: time for all nodes, −1 if any
  unreachable) with lazy-deletion heap pattern; efficiency test:
  50_000 edges. Also `shortest_route(n, edges, a, b)` returning
  the path (parent tracking).
- ex07 "k-stops-cheapest" — `cheapest_within_k_stops(n, flights,
  src, dst, k)` via k+1 rounds of edge relaxation on a COPIED dist
  array (docstring: why plain Dijkstra fails here).

## Checkpoint
"City infrastructure": given districts, candidate cable routes
(weighted), and project dependencies — `project_order(projects,
deps)` (topo or None/null), `cheapest_grid(n, routes)` (MST cost),
`fastest_signal(n, routes, hub)` (Dijkstra dist map),
`same_network(n, built_routes, queries)` (UF batch queries).
Efficiency test on the UF batch.

## SUMMARY.md
Cheat-sheet: algorithm-picker table (question → algorithm →
complexity), Kahn's template, UF template, Dijkstra template with
lazy-skip line highlighted, negative-edge warning box. Mindmap.
Self-quiz 8 Qs. Pattern-recognition drill: 8 one-liners spanning all
four tools + BFS decoy ("unweighted → module 15's BFS, not
Dijkstra").
