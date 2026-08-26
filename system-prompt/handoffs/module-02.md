# Handoff: Module 02 — Arrays & Dynamic Arrays

Build `02-arrays-dynamic-arrays/`. Read `CONVENTIONS.md` and the master
spec first. You own ONLY this folder.

Audience: completed module 01 (Big-O, framework, amortized-append
simulation). This module makes that simulation real.

## LESSON.md outline
1. Why this exists: the array is the structure everything else is
   measured against — O(1) index, O(n) insert/delete in the middle.
2. REQUIRED diagram: memory-layout graph of a static array (contiguous
   slots) vs what happens on insert-at-front (everything shifts).
3. Dynamic arrays: capacity vs length; the doubling resize; connect
   explicitly to module 01's `append_costs` exercise.
4. REQUIRED diagram: resize flowchart (push → full? → allocate 2×,
   copy, then write).
5. How to recognize it: "in place", "O(1) extra space", "shift/rotate/
   partition" → index gymnastics on arrays.
6. Template: the reader/writer two-index sweep (preview of module 04).
7. Worked example: dedupe-sorted traced in a state table.
8. Strings: immutable in most languages → build-then-join; O(n²) trap
   of repeated concatenation.
9. Gotchas: off-by-one, `length` vs `capacity`, aliasing vs copying.

## Exercises (exactly 6)
- ex01 "dynamic-array" — BUILD `DynamicArray`: fixed-capacity backing
  buffer (allocate with a fill value; in Python a list of `None`s
  created once — never `append` on it; in TS a pre-sized array),
  `push`, `pop`, `get(i)`/`set(i, v)` with bounds checks (raise/throw
  on bad index), `size()`, `capacity()`, doubling resize starting at
  capacity 1. FROM SCRATCH: the backing buffer may only be indexed,
  never grown by built-in append/push. Tests check capacity growth
  sequence 1→2→4→8 and amortized behavior (n = 100_000 pushes).
- ex02 "reverse-in-place" — `reverse(nums)` in place, O(1) space;
  `rotate_right(nums, k)` via the triple-reversal trick (k may exceed
  n). Tests forbid allocating a second array only behaviorally
  (correctness + docstring); include k=0, k=n, k>n.
- ex03 "remove-in-place" — `remove_value(nums, v)` → new length with
  survivors packed at front (order preserved, reader/writer);
  `dedupe_sorted(nums)` → new length, classic in-place dedupe.
- ex04 "merge-sorted-arrays" — `merge(a, b)` → new sorted array, O(m+n);
  `merge_into(a, m, b)` — a has spare capacity at the end, fill from
  the BACK, O(1) extra space.
- ex05 "string-drills" — `reverse_words(s)` ("one two" → "two one",
  collapse extra spaces), `run_length_encode(s)` ("aaabb" → "a3b2"),
  `run_length_decode(s)`; all O(n) using build-then-join.
- ex06 "matrix-walk" — `row_sums(grid)`, `col_sums(grid)`,
  `main_diagonal(grid)`, `transpose(grid)` (new grid, works for
  non-square). Establishes rows/cols indexing for later grid modules.

## Checkpoint
"Inventory shelf": a small `Shelf` class backed by the student's OWN
DynamicArray idea (re-implemented inside the checkpoint, simplified:
push/pop/get + doubling) plus free functions on plain arrays:
`restock_merge(a, b)` (merge sorted), `compact(slots)` (remove empties
in place, return count), `rotate_display(items, k)`. Tests include an
amortized push test (n = 50_000).

## SUMMARY.md
Cheat-sheet: array op-cost table (index/search/insert/delete,
front/middle/back), resize rules, in-place patterns list, string
building rule. Mindmap. Self-quiz 8 Qs. Pattern-recognition drill:
6 one-liners (answers: in-place two-index, dynamic array, string
build, matrix walk...).
