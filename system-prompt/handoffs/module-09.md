# Handoff: Module 09 — Sorting

Build `09-sorting/`. Read `CONVENTIONS.md` and the master spec first.
You own ONLY this folder.

Audience: completed modules 01–08 (recursion is fresh — merge/quick
build on it).

## LESSON.md outline
1. Why this exists: sorted data unlocks binary search, two pointers,
   greedy sweeps. Sorting is both a tool you call and a family of
   algorithms you must understand.
2. Elementary sorts in one section: insertion & selection, O(n²),
   when insertion sort is actually good (nearly-sorted, tiny n).
3. REQUIRED diagram: merge sort recursion tree (split to singletons,
   merge back up, log n levels × n work per level).
4. Quick sort: partition intuition. REQUIRED diagram: one Lomuto
   partition pass traced. Pivot choice, worst case, randomization.
5. Comparison table: insertion/selection/merge/quick/counting —
   time (best/avg/worst), space, stable?, in-place?
6. Stability: what it means, why multi-key sorting depends on it,
   worked two-key example.
7. Beyond comparisons: counting sort (bounded ints), bucket idea;
   the Ω(n log n) comparison lower bound in one honest paragraph.
8. Quickselect: partition without full sorting → O(n) average kth.
9. How to recognize it: "kth largest" → quickselect/heap; "custom
   order" → comparator; "values in a small range" → counting.
10. Gotchas: comparator consistency, sorting mutates vs copies
    (language-specific note), quick sort on sorted input.

## Exercises (exactly 6)
- ex01 "insertion-selection" — implement both on copies (return new
  array); tick-based test counts insertion-sort shifts on a
  nearly-sorted input (must be ~n, showing adaptivity).
- ex02 "merge-sort" — `merge_sort(nums)` returning a NEW sorted
  array; must be stable (tests sort (key, tag) pairs and check tag
  order). Efficiency test n = 200_000.
- ex03 "quick-sort" — in-place `quick_sort(nums)` with Lomuto
  partition + randomized pivot (accept any correct partition
  scheme); recursion on smaller side first mentioned in docstring.
  Efficiency test n = 200_000 including an already-sorted input
  (punishes fixed-first-pivot).
- ex04 "quickselect" — `kth_largest(nums, k)` average O(n) via
  partition (no full sort — tests use n = 200_000 with a generous
  op environment; also correctness for k = 1 and k = n).
- ex05 "counting-dutch-flag" — `counting_sort(nums, max_value)` for
  0..max_value ints, stable; `sort_colors(nums)` (0/1/2 in place,
  one pass, Dutch national flag three-pointer).
- ex06 "comparator-problems" — sorting as a solving tool:
  `largest_concat_number(nums)` (order by ab vs ba comparison →
  string answer, the classic "9,34,3" → "9343" puzzle; handle
  all-zeros), `sort_by_frequency(nums)` (freq asc, ties by value
  desc — pins multi-key + stability), `relative_order(nums, order)`
  (sort by position in a given ranking list, unknowns last,
  ascending).

## Checkpoint
"Tournament board": given player records (name, score, wins, joined) —
`rank_players(records)` multi-key stable sort (score desc, wins desc,
joined asc), `top_k_scores(records, k)` via quickselect idea (no full
sort of all n — efficiency test), `bucket_by_grade(scores)` counting
sort over 0..100.

## SUMMARY.md
Cheat-sheet: the comparison table (the module's centerpiece),
stability rule, quickselect template, comparator recipes per
language, "which sort when" decision flow. Mindmap. Self-quiz 8 Qs.
Pattern-recognition drill: 6 one-liners ("kth", "custom order",
"small value range", decoys).
