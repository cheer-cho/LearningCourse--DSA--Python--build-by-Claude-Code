# Handoff: Module 17 — Greedy & Intervals

Build `17-greedy-intervals/`. Read `CONVENTIONS.md` and the master
spec first. You own ONLY this folder.

Audience: completed modules 01–16 (sorting fluency assumed; heaps
available for meeting-rooms alternatives).

## LESSON.md outline
1. Why this exists: sometimes the locally best choice IS globally
   best — then you skip the exponential search entirely. The hard
   part is knowing when you're allowed to.
2. The exchange argument, informal: "if an optimal solution differs
   from greedy's choice, swap in greedy's choice — it never gets
   worse." One worked example (earliest-end-time interval picking).
   This is the thinking tool of the module — make it concrete.
3. REQUIRED diagram: Kadane's running along an array (current sum
   resets at negative prefixes), state table under it.
4. Greedy sweep patterns: running best (Kadane), furthest-reach
   (jump game), net-balance (gas station).
5. Intervals: ALWAYS sort first — but by start or by end? Rule:
   merging/overlap detection → by start; max-count selection → by
   end. REQUIRED diagram: timeline of intervals being merged.
6. How to recognize it: "maximum subarray", "can you reach",
   "minimum number of X to cover/schedule", intervals of any kind.
   Honesty box: greedy is easy to guess wrong — verify with the
   exchange argument or fall back to DP (module 18).
7. Gotchas: sorting by the wrong endpoint, touching vs overlapping
   (pin `[1,2],[2,3]`: touching, NOT overlapping — consistent
   course-wide), forgetting the empty/single-interval cases.

## Exercises (exactly 7)
- ex01 "kadane-max-run" — `max_subarray_sum(nums)` (Kadane, handles
  all-negative), `max_subarray_bounds(nums)` returning (best, start,
  end), `best_trades_unlimited(prices)` (sum of positive deltas —
  greedy proof sketch in docstring). Efficiency test.
- ex02 "jump-reach" — `can_reach_end(nums)` (furthest-reach sweep)
  and `min_jumps(nums)` (the current-window/next-window O(n)
  version — docstring contrasts with the DP O(n²)).
- ex03 "fuel-circuit" — `start_station(gas, cost)` → valid start
  index or −1; the "total ≥ 0 means one exists + reset on
  deficit" double insight, both argued in the docstring.
- ex04 "lifeboats" — `min_boats(weights, limit)` (sort + two
  pointers, 2 per boat) and `assign_kits(kits, needs)` (assign-
  cookies shape: satisfy most people, sort + two pointers).
- ex05 "merge-intervals" — `merge_intervals(intervals)` and
  `insert_interval(sorted_intervals, new)` (no re-sorting — the
  three-phase scan).
- ex06 "interval-scheduling" — `max_non_overlapping(intervals)`
  (sort by END — the exchange-argument showcase; docstring must
  argue it), `min_removals(intervals)` (= n − max), `can_attend_all(
  intervals)`, `min_rooms(intervals)` (start/end event sweep OR
  heap — accept both; efficiency test 100_000 intervals).
- ex07 "min-arrows" — `min_arrows(balloon_ranges)` (sort by end,
  shoot at end, touching counts as hit — pin it in tests).

## Checkpoint
"Conference planner": `plan_day(talks)` → max talks one person can
attend (by end), `rooms_needed(talks)`, `merge_busy(calendars)`
(merge many people's busy intervals), `coffee_run(energy_levels)`
(Kadane in disguise: best contiguous stretch of net energy).
Efficiency tests on rooms and merge.

## SUMMARY.md
Cheat-sheet: greedy pattern menu (running-best / furthest-reach /
net-balance / earliest-end), the sort-by-start-or-end rule, the
exchange-argument checklist ("would swapping ever hurt?"),
touching-vs-overlap pin. Mindmap. Self-quiz 8 Qs.
Pattern-recognition drill: 8 one-liners, INCLUDING two traps where
greedy fails and DP is needed (answers say "greedy fails here —
why?").
