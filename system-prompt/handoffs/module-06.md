# Handoff: Module 06 — Stacks & Queues

Build `06-stacks-queues/`. Read `CONVENTIONS.md` and the master spec
first. You own ONLY this folder.

Audience: completed modules 01–05. First "build a container with an
API" module since the dynamic array.

## LESSON.md outline
1. Why this exists: some problems only ever touch the MOST RECENT
   thing (undo, matching brackets, call stack) or the OLDEST thing
   (queues, BFS later). Restricting access makes O(1) guarantees
   possible.
2. REQUIRED diagram: stack push/pop (LIFO) next to queue
   enqueue/dequeue (FIFO), same 4 elements, different exit order.
3. Stack: array-backed, all ops O(1). The call stack connection.
4. Queue: why naive front-removal is O(n) on arrays; the circular
   buffer fix. REQUIRED diagram: ring buffer with head/tail wrapping.
5. How to recognize it: nesting/matching → stack; "most recent
   unresolved thing" → stack; processing in arrival order / shortest
   first by layers → queue; "next greater/smaller element" →
   monotonic stack.
6. Monotonic stack: keep the stack sorted by popping; each element
   pushed/popped once → O(n). Template + worked example: daily
   temperatures traced in a state table.
7. Gotchas: peeking empty, sentinel values, when to store indexes vs
   values (usually indexes).

## Exercises (exactly 7)
- ex01 "build-stack-queue" — BUILD `Stack` (array-backed: push/pop/
  peek/size/is_empty, underflow raises/throws) and `CircularQueue`
  (fixed-capacity ring buffer: enqueue/dequeue/front/size/is_full;
  enqueue on full raises/throws). FROM SCRATCH: backing storage is a
  pre-sized array; queue must NOT shift elements (tests do 100_000
  wrap-around ops to punish O(n) dequeue).
- ex02 "balanced-brackets" — `is_balanced(s)` for ()[]{} incl.
  interleaving traps ("([)]" false); `min_removals_to_balance(s)` for
  "()" only.
- ex03 "queue-via-stacks" — `QueueFromStacks`: two stacks, amortized
  O(1) dequeue; docstring ties back to module 01 amortized analysis.
- ex04 "min-stack" — `MinStack`: push/pop/peek/get_min all O(1)
  (auxiliary min stack). Tests interleave ops heavily.
- ex05 "postfix-eval" — `eval_postfix(tokens)` for + − * / with
  truncate-toward-zero division (document it; tests include
  negatives); `infix_hint` NOT required.
- ex06 "monotonic-warm-days" — `days_until_warmer(temps)` (daily
  temperatures, indexes on a monotonic stack) and
  `next_greater(nums)` → for each element its next greater value or
  −1. Efficiency test n = 200_000 on a worst-case
  monotonically-decreasing input.
- ex07 "histogram-max-rect" — HARD: `largest_rectangle(heights)` via
  monotonic stack with sentinel; docstring walks the "width =
  distance between smaller neighbors" insight. Efficiency test.

## Checkpoint
"Editor session": `EditorHistory` class — `type(text)`,
`delete_last()`, `undo()`, `redo()` (two stacks; new typing clears the
redo stack — the classic subtlety), plus `spans(prices)` (stock-span,
monotonic stack). Tests interleave undo/redo aggressively; efficiency
test on spans.

## SUMMARY.md
Cheat-sheet: stack vs queue op table, ring-buffer index math
(`(head + 1) % cap`), monotonic-stack template with the
"increasing-or-decreasing?" decision, store-index rule. Mindmap.
Self-quiz 8 Qs. Pattern-recognition drill: 8 one-liners (matching,
next-greater, arrival-order, plus decoys from earlier modules).
