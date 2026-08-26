# Handoff: Module 14 — Backtracking

Build `14-backtracking/`. Read `CONVENTIONS.md` and the master spec
first. You own ONLY this folder.

Audience: completed modules 01–13 (recursion is the hard
prerequisite; the call-tree mental model from module 08 becomes the
DECISION tree here).

## LESSON.md outline
1. Why this exists: some problems demand ALL valid combinations, or
   the needle in an exponential haystack. You can't loop your way
   through "every subset". You explore a decision tree — and undo.
2. REQUIRED diagram: decision tree for subsets of [1,2,3]
   (include/exclude branching), leaves labeled with the 8 subsets.
3. THE template (choose → explore → unchoose), annotated, with the
   path list mutation + copy-on-record trap called out.
4. The three classic shapes in one table: subsets (include/skip),
   combinations (for-loop with start index), permutations (used
   set / swap). When each applies.
5. Handling duplicates: sort + skip-same-choice-at-same-level.
   Worked example: subsets of [1,2,2] traced showing the skip.
6. Pruning: sort + break when candidate > remaining; constraint
   sets for N-queens. REQUIRED diagram: pruned branch marked on a
   combination-sum tree.
7. How to recognize it: "all combinations/permutations/ways to
   place/partition", "generate", small n (≤ ~20) as the tell.
8. Complexity honesty: 2ⁿ, n!, and why that's OK for small n.
9. Gotchas: forgetting to copy the path when recording, unchoose
   symmetry, duplicate handling level-vs-branch confusion.

## Exercises (exactly 7)
- ex01 "subsets-drill" — `subsets(nums)` (unique values) and
  `subsets_with_dup(nums)`. Tests order-insensitive.
- ex02 "combo-sum" — `combinations_of(n, k)` (1..n choose k) and
  `combination_sum(candidates, target)` (reuse allowed, unique
  candidates) with the prune-on-sorted optimization required
  (docstring explains it).
- ex03 "permutations-drill" — `permutations(nums)` and
  `permutations_unique(nums)` (with duplicates — level skip via
  counter map; docstring compares vs used-array).
- ex04 "phone-letters" — `letter_combos(digits)` (2–9 keypad
  mapping provided as a constant); empty input → empty list
  (pin it).
- ex05 "grid-word-search" — `exists_in_grid(board, word)`: DFS +
  backtrack with in-place visited marking and restore. Tests
  include a reuse-forbidden trap (word needs the same cell twice)
  and a full-grid snake path.
- ex06 "palindrome-partition" — `palindrome_partitions(s)` → all
  ways to split s into palindromic pieces.
- ex07 "n-queens" — HARD: `solve_n_queens(n)` → list of boards
  (list of strings with Q/.) using column/diagonal constraint
  SETS (not O(n) rescans — mention in docstring);
  `count_n_queens(n)`. Tests: n = 4 boards exactly, count for
  n = 8 → 92.

## Checkpoint
"Meal-plan builder": from a menu of (dish, cost) —
`all_plans_within_budget(menu, budget)` (subset shape with prune),
`plans_hitting_exact(menu, target, allow_repeats)` (combination-sum
shape), `tasting_orders(dishes)` (permutations of ≤ 8 unique
dishes). Tests order-insensitive; one pruning-required test (menu of
30 items where unpruned 2³⁰ is infeasible but prune + sorted costs
makes it instant — design carefully so the pruned version passes
fast).

## SUMMARY.md
Cheat-sheet: THE template, the three-shapes table, duplicate-skip
rule, pruning menu, copy-the-path rule. Mindmap. Self-quiz 8 Qs.
Pattern-recognition drill: 8 one-liners ("all ways" cues, small-n
tells, decoys that look exponential but are DP — flag them as
"coming in module 18").
