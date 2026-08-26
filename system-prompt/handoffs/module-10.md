# Handoff: Module 10 — Binary Search

Build `10-binary-search/`. Read `CONVENTIONS.md` and the master spec
first. You own ONLY this folder.

Audience: completed modules 01–09. Search-on-answer is the crown of
Part I — give it the most care.

## LESSON.md outline
1. Why this exists: sorted (or monotone) structure lets you discard
   half the possibilities per question → O(log n).
2. REQUIRED diagram: lo/hi/mid halving on a 16-element array, 3 steps.
3. THE template (pin one and stick to it course-wide):
   `lo, hi = 0, n` half-open, `while lo < hi`, `mid = lo + (hi-lo)//2`,
   answer = lo. Explain WHY this one avoids infinite loops and
   off-by-ones; show exact-match as a thin wrapper.
4. Boundary searches: first index ≥ x (lower bound), first index > x
   (upper bound); count occurrences = difference. Worked example
   traced in a table.
5. Rotated arrays: which half is sorted? Decision flowchart
   (REQUIRED diagram).
6. **Search on the answer**: the big idea — the array is imaginary;
   any monotone predicate `can(x)` over a numeric range is
   binary-searchable. How to recognize: "minimize the maximum...",
   "smallest capacity/speed/size such that...". Template:
   lo = min feasible, hi = max, search first x with can(x).
7. Worked example: min-rate problem end to end with the 5-step
   framework from module 01.
8. Gotchas: overflow note (language-specific honesty), open vs closed
   bounds mixing, predicate must actually be monotone.

## Exercises (exactly 7)
- ex01 "classic-search" — `binary_search(nums, target)` → index or −1
  using the course template; `count_occurrences(nums, target)` via
  two boundary calls.
- ex02 "boundaries" — `lower_bound(nums, x)`, `upper_bound(nums, x)`,
  `insert_position(nums, x)`; tests hammer duplicates, all-equal
  arrays, empty, x beyond both ends.
- ex03 "rotated-search" — `min_in_rotated(nums)` (unique values),
  `search_rotated(nums, target)`. Tests include rotation by 0.
- ex04 "rate-on-answer" — "min processing rate": machines process
  `piles` of jobs, one pile per hour at rate r; find min integer r
  to finish within h hours (Koko shape, renamed).
  `min_rate(piles, h)`; efficiency test with large piles.
- ex05 "capacity-on-answer" — "min truck capacity": ship packages in
  order within d days; `min_capacity(weights, d)`; also
  `split_min_largest(nums, k)` (split array minimizing the largest
  part — same predicate, say so in the docstring).
- ex06 "matrix-search" — `search_matrix(grid, target)`: rows sorted,
  first of each row > last of previous → one binary search over
  n·m as a flat index space.
- ex07 "peak-element" — `find_peak(nums)` O(log n) (neighbors
  distinct; walk uphill by comparing mid vs mid+1); docstring
  explains why an unsorted array can still be halved (the predicate
  is monotone along the chosen direction).

## Checkpoint
"Release bisector": `first_bad_build(n, is_bad)` (predicate function
injected — count calls, assert ≤ log₂(n)+2), `min_test_rigs(loads,
hours)` (search-on-answer), `find_version(tags, target)` (boundary
search over sorted tags with duplicates: first and last occurrence).

## SUMMARY.md
Cheat-sheet: THE template annotated line by line, boundary recipes,
rotated decision rules, search-on-answer checklist (range, predicate,
monotone proof), overflow note. Mindmap. Self-quiz 8 Qs.
Pattern-recognition drill: 8 one-liners — heavy on "minimize the max"
phrasing vs decoys.
