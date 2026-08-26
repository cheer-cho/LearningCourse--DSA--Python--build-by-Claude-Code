# Handoff: Module 08 — Recursion & Divide and Conquer

Build `08-recursion-divide-conquer/`. Read `CONVENTIONS.md` and the
master spec first. You own ONLY this folder.

Audience: completed modules 01–07. This module is the gateway to
trees, backtracking, and DP — teach the MENTAL MODEL hard.

## LESSON.md outline
1. Why this exists: some problems are defined in terms of smaller
   versions of themselves. Recursion lets the code mirror that
   definition.
2. REQUIRED diagram: the call tree of fib(5) (flowchart, repeated
   subtrees visually flagged) — this diagram gets reused
   conceptually in module 18.
3. The three rules: base case first; progress toward it; trust the
   recursive call (the "leap of faith" — spell this out, it is the
   thinking-process key).
4. The call stack: what actually happens; stack depth = space
   complexity; stack-overflow limits (mention language recursion
   limits honestly).
5. Recursion ↔ iteration: any recursion can become a loop + explicit
   stack. When you must (deep inputs).
6. Divide & conquer: split / solve halves / combine. REQUIRED
   diagram: merge-count flow on an 8-element array.
7. Memoization taste: cache fib → call count collapses (numbers
   shown); full framework promised for module 18.
8. Gotchas: missing base case, doing work before vs after the call,
   mutating shared state across calls.

## Exercises (exactly 6)
- ex01 "recursion-warmups" — `factorial(n)`, `sum_digits(n)`,
  `countdown(n)` → list [n..1] built recursively,
  `reverse_string_rec(s)`. Each docstring names base case and
  shrinking step explicitly (fill-in-the-plan style).
- ex02 "call-tree-fib" — `fib_naive(n, tick)` ticks once per call
  (tests assert exact call counts: fib_naive(10) → 177 calls);
  `fib_memo(n, tick)` ticks once per COMPUTED value (n+1 ticks).
  The student PROVES memoization works by the counter, not vibes.
- ex03 "fast-pow" — `power(x, n)` in O(log n) incl. negative n;
  `power_mod(base, exp, mod)` (needed later for Rabin-Karp — say
  so). Tick-based test asserts ~log₂(n) recursive calls.
- ex04 "nested-structures" — recursion on shape, not numbers:
  `deep_sum(nested)` (arbitrarily nested lists of ints),
  `max_depth_nested(nested)`, `flatten(nested)` → flat list in
  order. (Mirrors JSON walking; sets up tree recursion.)
- ex05 "merge-count-inversions" — divide & conquer:
  `count_inversions(nums)` via merge sort's merge (count cross
  pairs). Efficiency test n = 100_000 vs O(n²) infeasibility.
  Docstring: split/solve/combine named explicitly.
- ex06 "recursion-to-iteration" — given recursive reference versions
  IN COMMENTS, implement `deep_sum_iterative(nested)` and
  `countdown_iterative(n)` with an explicit stack; tests include an
  input deep enough to overflow naive recursion (document the
  depth chosen per language conservatively).

## Checkpoint
"File tree" (dicts/objects: name, size, children) —
`total_size(tree)`, `max_tree_depth(tree)`, `find_path(tree, name)` →
path list or None/null, `largest_file(tree)`. One deep-tree test
requiring the iterative technique OR language-safe recursion
(document). This checkpoint is deliberately module 11's warm-up.

## SUMMARY.md
Cheat-sheet: the three rules, call-stack cost table, D&C template,
recursion→iteration recipe, "when memo will matter" teaser table.
Mindmap. Self-quiz 8 Qs. Pattern-recognition drill: 6 one-liners
(self-similar structure cues vs plain-loop decoys).
