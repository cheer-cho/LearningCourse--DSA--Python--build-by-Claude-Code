# Handoff: Module 05 — Sliding Window

Build `05-sliding-window/`. Read `CONVENTIONS.md` and the master spec
first. You own ONLY this folder.

Audience: completed modules 01–04 (esp. two pointers and hashing —
this module fuses them).

## LESSON.md outline
1. Why this exists: "best subarray/substring of..." brute force checks
   O(n²) windows; a window that slides reuses work → O(n).
2. REQUIRED diagram: a window over an array with the incremental
   update shown (add entering element, remove leaving element).
3. Fixed-size windows: the add-one-drop-one loop.
4. Variable-size windows: grow the right edge every step; shrink the
   left edge while the window is invalid. REQUIRED diagram: flowchart
   of the grow/shrink loop.
5. How to recognize it: "longest/shortest/max/min substring or
   subarray that satisfies X", contiguous, and (for the shrink trick)
   X is monotone: growing never fixes a violation. Counter-example:
   negatives break sum-windows → prefix+hash (module 04 ex07).
6. Template: the canonical variable window with a hash-map state.
7. Worked example: longest-unique-run traced in a table (r, char,
   window, l moves).
8. Gotchas: shrink with `while` not `if`; update the answer at the
   right moment; window state must be O(1)-updatable.

## Exercises (exactly 7)
- ex01 "fixed-window-stats" — `max_window_sum(nums, k)`,
  `moving_averages(nums, k)`; the add/drop update, no re-summing
  (efficiency test n = 200_000, k = 1000).
- ex02 "best-trade" — `max_profit(prices)` (buy once, sell once):
  min-so-far sweep; frame it as a window whose left edge is "best
  buy so far". Include a falling-only prices test (answer 0).
- ex03 "longest-unique-run" — `longest_unique(s)` → length of longest
  substring without repeats (last-seen map or set+shrink).
  Efficiency test on a long repeating string.
- ex04 "longest-with-swaps" — `longest_uniform_with_k_edits(s, k)`
  (classic "character replacement"): window valid while
  size − max_freq ≤ k; docstring explains why max_freq may go stale
  without breaking correctness (the famous subtlety).
- ex05 "smallest-window-sum" — `shortest_subarray_at_least(nums,
  target)` with all-positive nums → shrink-while-valid variant
  (note the inversion: shrink while VALID to find the shortest).
  Efficiency test.
- ex06 "window-anagram" — `contains_permutation(needle, haystack)`:
  fixed window + frequency compare with an O(1) "matches" counter
  (not re-comparing 26 counts per step — tests use long inputs).
- ex07 "min-cover-window" — HARD: `min_window_cover(s, t)` → smallest
  substring of s containing every char of t with multiplicity ("" if
  none). need/have counters + shrink-while-satisfied. Efficiency
  test.

## Checkpoint
"Traffic monitor": given per-second request counts and an
allowed-burst budget — `worst_minute(counts)` (fixed window 60),
`longest_within_budget(counts, budget)` (variable window, sum ≤
budget, all counts ≥ 0), `shortest_breach(counts, threshold)`
(shortest window with sum ≥ threshold), `has_pattern_burst(counts,
pattern)` (permutation-in-string shape on small int alphabet).
Efficiency tests.

## SUMMARY.md
Cheat-sheet: fixed vs variable template side by side, the
monotonicity rule ("when growing can't fix it, slide"), window-state
menu (sum, count map, max_freq, need/have), decision note "negatives →
prefix+hash". Mindmap. Self-quiz 8 Qs. Pattern-recognition drill: 8
one-liners mixing window, two-pointer, prefix, hash cues.
