# Handoff: Module 01 — Big-O & Foundations

Build `01-big-o-foundations/`. Read `CONVENTIONS.md` (same folder) and
the master spec first. You own ONLY this folder. Slugs below are
language-neutral; CONVENTIONS.md maps them to filenames.

Audience: knows the host language well (this is a DSA course, not a
language course) but has NEVER studied algorithms formally. Zero DSA
assumed. No other module exists yet — use only plain
lists/arrays/dicts/Maps and loops.

## LESSON.md outline
1. Why this exists: two programs give the same answer; one takes 1 ms,
   the other an hour. Complexity is how we predict which — before
   running anything.
2. The RAM model in one paragraph: reads/writes/arithmetic cost 1 "op".
3. REQUIRED diagram: flowchart/graph of growth curves ranking
   O(1) → O(log n) → O(n) → O(n log n) → O(n²) → O(2ⁿ) with a
   "n = 1,000,000 → how many ops?" table beside it.
4. Reading complexity from code: sequential = add, nested = multiply,
   halving = log. Small worked examples of each.
5. Space complexity: extra memory, not input memory.
6. Amortized cost, intro only: sometimes one expensive op is fine if
   it is rare (teaser for the dynamic array in module 02).
7. **The 5-step problem-solving framework** (REQUIRED diagram —
   flowchart): understand & restate → brute force out loud → find the
   bottleneck → apply a pattern/structure → verify with edge cases.
   Tell the student every later module hangs off step 4.
8. Gotchas: constants don't matter (until they do), best/worst/average,
   "n" must be named (n of what?).

## Exercises (exactly 5)
- ex01 "growth-rates" — the file shows 8 short code snippets in
  comments; student fills a returned dict/record mapping snippet name →
  complexity string from a fixed answer set ("O(1)", "O(log n)",
  "O(n)", "O(n log n)", "O(n^2)", "O(2^n)"). Tests assert exact
  answers.
- ex02 "count-ops" — functions receive a `tick()` callback and must
  call it once per "unit of work": `sum_all(nums, tick)` (n ticks),
  `all_pairs(items, tick)` (n² ticks), `halve_down(n, tick)`
  (⌊log₂ n⌋+1 ticks). Tests count ticks for several sizes — the
  student SEES growth rates instead of reading about them.
- ex03 "naive-vs-fast" — `has_duplicate_naive(nums, tick)` must be the
  O(n²) all-pairs version (tick per comparison, tests assert the count
  to force honesty), then `has_duplicate_fast(nums)` O(n) with a
  set. Efficiency test: n = 200_000 on the fast one.
- ex04 "amortized-append" — simulate a doubling dynamic array:
  `append_costs(n)` returns the per-append cost list (1, or
  current_size+1 when full, starting capacity 1); `total_cost(n)`;
  tests assert total_cost(n) ≤ 3n for several n. Teaches amortized
  O(1) with numbers, not hand-waving.
- ex05 "target-pair" — apply the framework end to end:
  `has_pair_brute(nums, target)` O(n²), then
  `has_pair_fast(nums, target)` O(n) using a set of complements.
  Efficiency test on the fast version. Docstring walks the 5 steps.

## Checkpoint
"Performance review": given three tasks —
- `most_common(words)` → the most frequent word in O(n) (counting
  with a dict/Map; ties broken by first occurrence);
- `first_repeated(nums)` → first value seen twice, O(n);
- `complexity_report()` → dict/record answering 5 classification
  questions about the two functions above and three shown snippets.
Efficiency tests on both functions (n = 200_000).

## SUMMARY.md
Cheat-sheet: complexity table with real-world op counts, "reading
complexity from code" rules, the 5-step framework as a numbered list.
Mindmap. Self-quiz 8 Qs. Pattern-recognition drill: 5 one-liners where
the answer is a complexity class, not a pattern (this module's
version of the drill).
