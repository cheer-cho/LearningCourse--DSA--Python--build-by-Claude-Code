# Handoff: Module 12 — Heaps & Priority Queues

Build `12-heaps-priority-queues/`. Read `CONVENTIONS.md` and the
master spec first. You own ONLY this folder.

Audience: completed modules 01–11 (trees make "complete binary tree
in an array" natural).

Language note: ex01 BUILDS the heap — no `heapq` (Python) and no
library heap (TS). From ex03 on, Python exercises may use `heapq`;
TypeScript exercises ship a small PROVIDED (not stubbed) `MinHeap`
inside the exercise file — copy the reference implementation from
ex01's solution, marked "provided — do not edit".

## LESSON.md outline
1. Why this exists: "give me the smallest/largest RIGHT NOW, and keep
   taking them" — full sorting is overkill; a heap does push/pop in
   O(log n) and peek in O(1).
2. REQUIRED diagram: complete binary tree drawn above its array form,
   with the index math labeled (parent (i−1)//2, children 2i+1,
   2i+2).
3. The heap property (min-heap: parent ≤ children) — NOT sorted, and
   that's the point.
4. Sift up (push) and sift down (pop) walked step by step.
   REQUIRED diagram: one sift-down after a pop.
5. Heapify bottom-up in O(n) — one honest paragraph on why it isn't
   O(n log n).
6. How to recognize it: "kth largest/smallest", "top k", "k closest",
   "merge k sorted", "running median", "schedule by priority".
   The k-size-heap trick: keep a MIN-heap of size k for top-k
   LARGEST (spell out the inversion — it trips everyone).
7. Worked example: top-3 of a stream traced in a table.
8. Gotchas: min vs max (negate or comparator), heap of tuples/pairs
   for tie-breaking, lazy deletion idea (mention only).

## Exercises (exactly 7)
- ex01 "build-min-heap" — BUILD `MinHeap`: `push/pop/peek/size` +
  classmethod/static `heapify(nums)` bottom-up. FROM SCRATCH (no
  library heap). Tests: random-op fuzz vs a sorted-list oracle
  (1_000 ops), heapify O(n) correctness, pop order on duplicates.
- ex02 "heap-sort" — `heap_sort(nums)` → new sorted array using the
  student's heap idea (either via MinHeap pops or in-place max-heap
  variant; accept both). Efficiency test n = 100_000.
- ex03 "top-k-frequent" — `top_k_frequent(nums, k)` (count + heap of
  size k; any-order answer). Efficiency test n = 200_000, k = 10 —
  infeasible for sort-everything? sort is n log n, fine; the test
  just checks correctness at scale. Docstring: compare heap
  O(n log k) vs sort O(n log n) vs bucket O(n).
- ex04 "k-closest-points" — `k_closest(points, k)` to origin,
  size-k max-heap (or heapify-all — docstring compares); squared
  distance, no sqrt (say why).
- ex05 "kth-largest-stream" — class `KthLargest(k, initial)` with
  `add(val)` → kth largest so far; min-heap of size k. Efficiency
  test: 100_000 adds.
- ex06 "running-median" — HARD: `MedianFinder`: `add(num)` /
  `median()` via two balanced heaps (max-heap lows, min-heap highs);
  docstring walks the rebalance invariant. Efficiency test 100_000
  adds with interleaved median calls.
- ex07 "merge-k-sorted" — `merge_k_sorted(lists)` → one sorted array
  via heap of (value, list_idx, elem_idx); efficiency test: 1_000
  lists × 100 elements. Docstring compares vs pairwise merging.

## Checkpoint
"ER triage": `TriageQueue` — `arrive(name, severity, timestamp)`,
`next_patient()` (highest severity first, FIFO within severity — pin
the tie-break with a tuple key), `waiting_count()`; plus
`k_most_urgent(records, k)` free function. Efficiency test 100_000
ops.

## SUMMARY.md
Cheat-sheet: index math, op-cost table, the top-k inversion rule
("want largest → keep min-heap of size k"), tuple-key tie-breaking,
heapq/API mapping for the language. Mindmap. Self-quiz 8 Qs.
Pattern-recognition drill: 8 one-liners ("kth", "top k", "streaming",
decoys: "kth in sorted array" → just index; "single max" → one pass).
