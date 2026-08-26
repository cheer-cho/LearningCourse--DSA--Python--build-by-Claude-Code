# Handoff: Module 07 — Linked Lists

Build `07-linked-lists/`. Read `CONVENTIONS.md` and the master spec
first. You own ONLY this folder.

Audience: completed modules 01–06 (needs hashing for LRU, stacks for
contrast).

Node convention (pin it): exercises define their own `ListNode`
(value + next; doubly adds prev) in the file where it's built; later
exercises in THIS module may import it from ex01's file. Provide
`from_array`/`to_array` helpers in ex01 — every later test uses them
to build and inspect lists, so get them right first.

## LESSON.md outline
1. Why this exists: arrays pay O(n) to insert in the middle; linked
   lists pay O(1) — if you already hold the node. The trade: no O(1)
   indexing.
2. REQUIRED diagram: nodes with next-arrows; show an O(1) middle
   insert vs the array shift.
3. Array vs linked list comparison TABLE (index, search,
   insert/delete at front/middle/back, cache friendliness).
4. Pointer surgery rules: draw before you code; order of reassignment
   matters; dummy/sentinel head removes edge cases.
5. How to recognize it: problem hands you a list/chain of nodes;
   "O(1) removal given the node"; LRU-style "move to front".
6. Fast & slow pointers: middle, cycle detection (Floyd), why the
   meet-point math works (short informal argument + diagram —
   REQUIRED diagram: cycle with hare/tortoise positions).
7. Worked example: in-place reversal traced node by node (prev, cur,
   next table).
8. Gotchas: losing the rest of the list, off-by-one around dummy
   heads, forgetting to null the tail.

## Exercises (exactly 7)
- ex01 "build-singly-list" — `ListNode` + `SinglyLinkedList`:
  `push_front/push_back/pop_front/find/delete_value/size/to_array`
  and module-level `from_array/to_array` helpers. Track a tail
  pointer so push_back is O(1) (tests check 100_000 push_backs).
- ex02 "reverse-list" — `reverse_list(head)` iterative O(1) space;
  `reverse_list_recursive(head)`; both return the new head.
- ex03 "fast-slow" — `middle_node(head)` (second middle for even
  lengths — pin it in tests), `has_cycle(head)`,
  `cycle_start(head)` (Floyd phase 2). Test helpers build cyclic
  lists by index.
- ex04 "merge-two-lists" — `merge_sorted(a, b)` splicing nodes (no new
  nodes — tests assert node identity where the language allows),
  `remove_nth_from_end(head, n)` one pass with a gap pointer + dummy.
- ex05 "reorder-list" — `reorder(head)`: L0→Ln→L1→Ln−1... in place =
  middle + reverse second half + interleave. The "combine your
  moves" exercise; docstring lists the three sub-steps as the plan.
- ex06 "build-doubly-list" — `DoublyLinkedList` with head/tail
  SENTINELS: `push_front/push_back/pop_front/pop_back/remove_node
  (O(1) given the node)/to_array`. Docstring: sentinels mean no
  null-checks anywhere — the point of the exercise.
- ex07 "lru-cache" — BUILD `LRUCache(capacity)`: `get/put` both O(1)
  = hash map → node + doubly list with sentinels (re-implement or
  import from ex06). Evict least-recent on overflow; get refreshes
  recency. Efficiency test: 100_000 mixed ops, capacity 500.

## Checkpoint
"Music queue": `PlayQueue` on a doubly linked list — `add_last(song)`,
`play_next()` (pop front), `play_now(song)` (push front),
`remove(song)` (first match), `history(k)` — PLUS `recently_played`
behavior capped at k using LRU eviction logic. Mixed-op efficiency
test.

## SUMMARY.md
Cheat-sheet: array vs list table (again, condensed), pointer-surgery
checklist, dummy-node rule, fast/slow recipes (middle, cycle, gap-k),
LRU anatomy diagram-in-words. Mindmap. Self-quiz 8 Qs.
Pattern-recognition drill: 7 one-liners (fast/slow cues, O(1)-removal
cues, decoys).
