# Handoff: Module 19 — Dynamic Programming II (2-D)

Build `19-dp-2d/`. Read `CONVENTIONS.md` and the master spec first.
You own ONLY this folder.

Audience: completed modules 01–18. The framework from module 18 is
assumed cold; this module scales the STATE to two dimensions.

## LESSON.md outline
1. Why this exists: when one index can't describe the state —
   position in TWO strings, item index AND remaining capacity — the
   dp table grows a dimension. Same framework, bigger table.
2. REQUIRED diagram: LCS grid for "ace" × "abcde" fully filled,
   arrows showing where each cell's value came from (match ↖ vs
   max of ← ↑).
3. The two big 2-D families, as a table:
   - two-sequences (LCS, edit distance): dp[i][j] = answer for
     prefixes i and j;
   - item-and-budget (knapsack): dp[i][cap] = best using first i
     items within cap.
4. Worked example: 0/1 knapsack through the 5 framework steps,
   small table filled by hand. The take-it-or-leave-it recurrence.
5. 0/1 vs unbounded knapsack: ONE line of code difference
   (iteration direction / which row you read) — make this the "aha"
   and show both.
6. Space optimization: 2 rows, then 1 row with reverse iteration
   for 0/1 (why reverse — spelled out; this is a classic interview
   probe).
7. How to recognize it: two strings compared → two-sequence DP;
   "pick items under a limit" → knapsack; "count ways to make X
   from parts" → unbounded; grid movement costs → grid DP.
8. Gotchas: row/col off-by-one (the +1 border), iterating capacity
   in the wrong direction, confusing "subsequence" (LCS) with
   "substring".

## Exercises (exactly 7)
Framework comment (5 one-liners) required in every solution, same as
module 18.

- ex01 "grid-paths" — `count_paths(rows, cols)`,
  `count_paths_blocked(grid)` (obstacles), `min_path_cost(grid)`.
  One-row space optimization required on ex01's first function
  (docstring says so; tests can't see it — verify in solution).
- ex02 "common-subsequence" — `lcs_length(a, b)` and
  `lcs_string(a, b)` (reconstruct by walking the table back).
  Efficiency test: two 1_000-char strings.
- ex03 "edit-distance" — `edit_distance(a, b)` (insert/delete/
  replace); docstring maps each of the three table-moves to its
  edit operation explicitly (the understanding check).
- ex04 "knapsack-01" — `max_value(weights, values, capacity)` and
  `can_partition_equal(nums)` (subset-sum reduction — the docstring
  must present the reduction as the point). 1-D reverse-iteration
  version required for can_partition_equal.
- ex05 "knapsack-unbounded" — `count_coin_ways(coins, amount)`
  (coin change II — combinations not permutations: coins outer
  loop; docstring contrasts with module 18 checkpoint's
  order-matters variant) and `max_ribbon_value(lengths, prices,
  total)` (rod-cutting shape).
- ex06 "target-sum-ways" — `ways_to_target(nums, target)` (+/−
  signs → subset-sum count reduction, derived in the docstring;
  handle odd/impossible and zeros).
- ex07 "palindrome-dp" — `count_palindromic_substrings(s)` and
  `longest_palindromic_substring(s)` via expand-around-center
  (docstring compares O(n²)/O(1)-space expansion vs the O(n²)
  table; either accepted for the second function). Efficiency
  test: 2_000-char string.

## Checkpoint
"Product launch": `best_feature_set(costs, impacts, budget)` (0/1
knapsack picking WHICH features too — reconstruct one optimal set),
`slogan_similarity(a, b)` (edit distance), `bundle_ways(pack_sizes,
order_size)` (unbounded count), `is_fair_split(workloads)`
(partition). Efficiency test on the knapsack (50 items × capacity
10_000, 1-D array required to fit time comfortably).

## SUMMARY.md
Cheat-sheet: the two-family table, knapsack 0/1-vs-unbounded
one-liner diff highlighted, space-optimization ladder (full → 2 rows
→ 1 row + direction rule), reduction gallery (partition, target
sum). Mindmap. Self-quiz 8 Qs. Pattern-recognition drill: 8
one-liners across both families + 1-D decoys.
