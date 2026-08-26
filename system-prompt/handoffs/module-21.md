# Handoff: Module 21 — Advanced Structures & String Algorithms

Build `21-advanced-structures-strings/`. Read `CONVENTIONS.md` and
the master spec first. You own ONLY this folder.

Audience: completed modules 01–20. This is the "senior-level
differentiators" module — the lesson should say honestly WHERE these
actually appear (range-query problems, competitive-style hards,
"design a metrics service" system questions) and that they're asked
less often than Parts I–II but separate strong candidates.

## LESSON.md outline
1. Why this exists: prefix sums (module 04) die the moment data
   UPDATES. Segment trees and Fenwick trees give O(log n) for both
   update and range query. And naive substring search is O(n·m);
   rolling hashes and failure functions make it O(n+m).
2. Segment tree: REQUIRED diagram — the tree over an 8-element
   array, each node labeled with its range and sum; one query's
   visited nodes highlighted. Build/query/update walked; the
   "merge function" generalization (sum → min → max = same tree).
3. Fenwick (BIT): the lowbit trick; smaller/faster but
   prefix-only mindset. Comparison table: prefix array vs Fenwick
   vs segment tree (build, update, range query, code size).
4. Monotonic deque: sliding-window maximum in O(n). REQUIRED
   diagram: deque contents evolving over a window slide (link back
   to module 06's monotonic stack — this is its two-ended sibling).
5. Rabin-Karp: rolling hash (add a char, drop a char in O(1)),
   collision honesty (verify on hash hit), the mod-pow connection
   to module 08's `power_mod`.
6. KMP: the failure/prefix function as "longest border"; walked on
   "ababaca" in a table; then the search loop. Keep it gentle —
   this is the hardest 30 lines in the course; the diagram-first
   rule matters most here.
7. How to recognize it: "updates AND range queries" → segment/
   Fenwick; "max of each window" → monotonic deque; "find/count
   pattern occurrences, huge text" → KMP/Rabin-Karp.
8. Gotchas: segment-tree index arithmetic, forgetting to verify on
   hash match, failure-table off-by-one.

## Exercises (exactly 6)
- ex01 "build-segment-tree" — BUILD `SegmentTree(nums)` (array-
  based, 4n storage): `range_sum(i, j)` inclusive,
  `update(i, value)`. Efficiency test: n = 100_000, 50_000 mixed
  ops vs naive infeasibility.
- ex02 "range-min-tree" — generalize: `RangeMinTree` (same skeleton,
  min merge) answering `range_min(i, j)` + `update`; docstring:
  what changed vs ex01 (merge fn + identity element) — the
  abstraction is the lesson.
- ex03 "build-fenwick" — BUILD `Fenwick(n)`: `add(i, delta)`,
  `prefix_sum(i)`, `range_sum(i, j)`; lowbit loops. Then
  `count_smaller_after(nums)` using it over compressed values
  (HARD part, well-scaffolded docstring). Efficiency test.
- ex04 "window-max-deque" — `window_maxes(nums, k)` via monotonic
  deque (store indexes; evict stale front, pop smaller backs).
  Efficiency test n = 200_000 vs O(nk) naive.
- ex05 "rabin-karp" — `find_all(text, pattern)` → all match indexes
  via rolling hash + verification; `count_repeated_windows(dna, k)`
  (repeated k-length substrings — hash-set of rolling hashes).
  Efficiency test on a 200_000-char text.
- ex06 "kmp-search" — `failure_table(pattern)` (tested separately —
  the table IS the understanding) and `kmp_find_all(text,
  pattern)`. Worst-case efficiency test ("aaaa..." text,
  "aaab" pattern) that punishes naive rescanning.

## Checkpoint
"Metrics service": `MetricsBoard(initial_values)` — `record(i, v)`
(point update), `window_total(i, j)`, `window_low(i, j)` (two trees
inside), plus `alert_scan(log_text, signature)` (KMP or Rabin-Karp —
student's choice, docstring must name which and why) and
`busiest_window(readings, k)` (max window sum via deque or prefix —
their choice). Efficiency tests on both halves.

## SUMMARY.md
Cheat-sheet: the three-range-tools comparison table, deque template,
rolling-hash recipe with the drop-char formula, failure-table
walkthrough mini-example, "where these appear in interviews" honesty
box. Mindmap. Self-quiz 8 Qs. Pattern-recognition drill: 6
one-liners (update+query cues, window-max, pattern-in-text, decoys
solved by module 04/05 tools).
