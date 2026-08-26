# Handoff: Module 18 — Dynamic Programming I (1-D)

Build `18-dp-1d/`. Read `CONVENTIONS.md` and the master spec first.
You own ONLY this folder.

Audience: completed modules 01–17. Module 08's call-tree diagram and
fib-with-counters exercise are the emotional setup — reference them.

## LESSON.md outline
1. Why this exists: backtracking explores the whole decision tree;
   DP notices the tree asks the SAME questions repeatedly and
   answers each once. Exponential → polynomial.
2. THE framework (the module's centerpiece — everything else is
   instances of it):
   1. Define the STATE in words ("dp[i] = best answer for the first
      i items").
   2. Find the CHOICE at each state.
   3. Write the RECURRENCE.
   4. Pin BASE CASES.
   5. Pick the ORDER (memo top-down or table bottom-up).
   REQUIRED diagram: this framework as a flowchart.
3. Memoization vs tabulation side-by-side on climbing stairs (both
   code skeletons), comparison table (stack depth, ease, space
   optimization). Space optimization: keep two variables when
   dp[i] only needs dp[i−1], dp[i−2].
4. REQUIRED diagram: the fib/stairs call tree from module 08 with
   memoized nodes collapsed — "this is the whole trick".
5. Worked example: house robber through all 5 framework steps,
   state table filled in.
6. How to recognize it: "count the ways", "min/max cost to reach",
   "can it be done" + overlapping choices + no need to enumerate
   the actual combinations (vs backtracking which must).
7. Gotchas: state too vague ("best so far" of WHAT?), iteration
   order violating dependencies, initializing with 0 vs ±infinity,
   off-by-one between "first i items" and index i.

## Exercises (exactly 7)
Every solution's comment block MUST state the framework's 5 parts in
one line each — this module enforces the thinking process hardest.

- ex01 "stairs-framework" — `climb_ways(n)` four times:
  `_naive(n, tick)` (tick per call, tests assert exponential-ish
  counts for small n), `_memo(n, tick)` (≤ 2n ticks), `_table(n)`,
  `_optimized(n)` (O(1) space). The framework materialized.
- ex02 "min-cost-stairs" — `min_cost_climb(costs)` (start at 0 or
  1, land past the end). First "min instead of count" transfer.
- ex03 "robber-houses" — `max_loot(values)` (house robber) and
  `max_loot_circle(values)` (circular: max of two linear runs —
  the reduction argued in the docstring).
- ex04 "coin-min" — `min_coins(coins, amount)` (−1 if impossible;
  unbounded choice per state; initialize with infinity). Efficiency
  test amount = 10_000, awkward coin set. Docstring: why greedy
  biggest-coin fails (link back to module 17's honesty box) with
  the [1,3,4], 6 counter-example in tests.
- ex05 "word-split" — `can_segment(s, words)` (word break; dp[i] =
  prefix of length i splittable; word set for O(1) lookup).
  Efficiency test: adversarial "aaaa...b" input.
- ex06 "decode-count" — `decode_ways(digits)` ("12" → 2): the
  edge-case gauntlet — leading zeros, "10", "27", "100". State the
  two-choice recurrence cleanly.
- ex07 "longest-rising" — `lis_length(nums)` O(n²) DP first, then
  `lis_length_fast(nums)` O(n log n) tails + lower_bound (import
  nothing — reuse the module-10 template inline; docstring
  explains why tails works). Efficiency test n = 100_000
  distinguishes them.

## Checkpoint
"Freelancer calendar": jobs along a line of days —
`max_earnings(day_pay)` (non-adjacent picks = robber),
`min_gear_cost(day_costs)` (min-cost climb shape),
`ways_to_fill(n_days, block_sizes)` (count compositions with given
block sizes = coin-change-count variant, order matters — pin
semantics in docstring), `longest_growth_streak(revenues)` (LIS).
Efficiency test on the LIS part.

## SUMMARY.md
Cheat-sheet: THE framework numbered 1–5, memo vs table table,
space-optimization rule, "count vs min vs can" recurrence templates,
greedy-vs-DP decision note. Mindmap. Self-quiz 8 Qs.
Pattern-recognition drill: 8 one-liners (DP cues vs backtracking
"enumerate them all" cues vs greedy-safe cues).
