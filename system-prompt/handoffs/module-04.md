# Handoff: Module 04 — Two Pointers & Prefix Sums

Build `04-two-pointers-prefix-sums/`. Read `CONVENTIONS.md` and the
master spec first. You own ONLY this folder.

Audience: completed modules 01–03 (Big-O, arrays, hashing).

## LESSON.md outline
1. Why this exists: nested loops scan pairs in O(n²); when the data is
   sorted (or the move rule is monotone), two indexes moving toward
   each other find the same answer in O(n).
2. REQUIRED diagram: opposite-ends pointers on a sorted array closing
   in on a target (show 2–3 steps with the "sum too big → move right
   pointer left" rule).
3. How to recognize it: sorted input + pair/triplet target; "in
   place"; palindrome checks; partition/segregate; reader/writer
   compaction.
4. Templates: opposite-ends loop; same-direction reader/writer loop.
5. Worked example: sorted pair-sum step table (l, r, sum, move).
6. Prefix sums: precompute once (O(n)), answer any range sum in O(1).
   REQUIRED diagram: array with its prefix array above it, one range
   query shown as prefix[j+1] − prefix[i].
7. How to recognize prefix sums: "sum of a range", "how many subarrays
   with sum X", "equal split point".
8. Gotchas: pointer crossing conditions (< vs <=), duplicate skipping
   in 3-sum, prefix index off-by-one (size n+1 array).

## Exercises (exactly 7)
- ex01 "sorted-pair-target" — `pair_sum_sorted(nums, target)` → indices
  in a SORTED array via opposite ends, O(1) space; contrast with
  module 03's hash version in the docstring. Efficiency test.
- ex02 "valid-palindrome" — `is_clean_palindrome(s)`: ignore
  non-alphanumeric, case-insensitive, two pointers;
  `valid_after_one_delete(s)` (classic 680, first "greedy branch"
  taste).
- ex03 "move-zeroes" — `move_zeroes(nums)` in place, order of non-zeros
  preserved (reader/writer); `partition_even_odd(nums)` (evens first,
  any order, opposite ends swap).
- ex04 "triplet-sum" — `three_sum_zero(nums)` → all unique triplets
  summing to 0; sort + fixed first element + opposite-ends inner scan
  + duplicate skipping. O(n²). Tests are order-insensitive.
- ex05 "container-water" — classic max-area: `max_container(heights)`;
  docstring must walk WHY moving the shorter side is safe (the
  exchange argument, informal). Efficiency test n = 200_000.
- ex06 "prefix-ranges" — `build_prefix(nums)` (length n+1);
  `RangeSum` class: constructor precomputes, `query(i, j)` inclusive
  O(1); `pivot_index(nums)` (left sum == right sum). Efficiency test:
  100_000 queries on n = 100_000.
- ex07 "subarray-sum-k" — `count_subarrays_with_sum(nums, k)` O(n):
  prefix sum + hash map of prefix counts (works with negatives —
  tests include them, which kills the future sliding-window approach;
  say so in the docstring). Efficiency test.

## Checkpoint
"Elevation survey": given an elevation profile (array of ints) —
`flat_pairs(sorted_readings, target)` (two pointers),
`compact_gaps(readings)` (in-place remove of sentinel values),
`range_gain(readings)` → object answering `query(i, j)` net gain in
O(1), `balanced_checkpoint(readings)` (pivot index). Efficiency tests
on the query path.

## SUMMARY.md
Cheat-sheet: the two pointer templates side by side, when-sorted-
matters rule, prefix recipe with the n+1 convention, "negatives? →
prefix+hash, all positive? → sliding window (next module)" decision
note. Mindmap. Self-quiz 8 Qs. Pattern-recognition drill: 8 one-liners
mixing two-pointer, prefix-sum, and hash cues.
