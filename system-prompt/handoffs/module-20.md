# Handoff: Module 20 — Bit Manipulation & Math

Build `20-bit-manipulation-math/`. Read `CONVENTIONS.md` and the
master spec first. You own ONLY this folder.

Audience: completed modules 01–19. A breather module after DP — two
compact toolkits interviews expect.

Language note (be honest in the lesson): Python ints are arbitrary
precision (masking with & 0xFFFFFFFF emulates 32-bit); JS/TS bitwise
ops work on 32-bit signed ints (>>> vs >> matters). Each repo's
lesson covers ITS language's reality.

## LESSON.md outline
1. Why this exists: numbers ARE bit arrays. Some problems collapse
   from O(n) space to O(1) when you treat them that way — and
   interviewers use bits to probe fundamentals.
2. REQUIRED diagram: the number 13 as bits with place values; AND/
   OR/XOR/shift shown as row operations on two bit rows.
3. The toolkit, each with a one-line recipe: get bit, set bit,
   clear bit, toggle, lowest set bit (n & −n), drop lowest set bit
   (n & (n−1)), is power of two.
4. XOR's three superpowers: a^a=0, a^0=a, order doesn't matter →
   canceling pairs, finding the odd one out, swap-free diffing.
5. Worked example: single-number traced (XOR fold over the array).
6. Math essentials: Euclid's gcd (with the WHY in two sentences),
   lcm via gcd, fast pow (link back to module 08), primality by
   √n trial + sieve of Eratosthenes. REQUIRED diagram: sieve
   crossing out multiples on a 2–30 grid.
7. Matrix as math: rotate 90° = transpose + reverse rows (diagram
   optional third), spiral = four shrinking bounds.
8. How to recognize it: "without extra memory", "appears once/twice",
   "count set bits", divisibility/primes, in-place matrix moves.
9. Gotchas: operator precedence (& vs ==), negative shifts,
   sign-bit surprises (language-specific), integer division vs
   float.

## Exercises (exactly 6)
- ex01 "bit-basics" — `get_bit(n, i)`, `set_bit(n, i)`,
  `clear_bit(n, i)`, `toggle_bit(n, i)`, `is_power_of_two(n)`,
  `count_set_bits(n)` (Kernighan n&(n−1) loop — tick-test asserts
  loop count equals the number of set bits, not bit width).
- ex02 "xor-tricks" — `find_single(nums)` (all twice but one),
  `find_missing(nums)` (0..n with one gap — XOR version required;
  docstring mentions the sum alternative and its overflow caveat),
  `swap_count_bits(a, b)` → Hamming distance a^b.
- ex03 "bit-tables" — `count_bits_upto(n)` → list 0..n via the
  dp[i] = dp[i>>1] + (i&1) recurrence (docstring derives it —
  it's secretly DP, say so), `reverse_bits32(n)` (32-bit).
- ex04 "math-essentials" — `gcd(a, b)` (Euclid, iterative),
  `lcm(a, b)`, `primes_upto(n)` (sieve; efficiency test
  n = 1_000_000), `is_prime(n)` (√n trial division).
- ex05 "matrix-moves" — `rotate_90_in_place(grid)` (square,
  transpose+reverse), `spiral_order(grid)` (any rectangle),
  `zero_rows_cols(grid)` in place using first row/col as markers
  (O(1) extra space — the classic trick, docstring walks it).
- ex06 "digit-strings" — `add_binary(a, b)` (binary strings, no
  built-in bigint parse of the whole string — carry loop),
  `plus_one(digits)` (digit array), `is_happy(n)` (cycle detection
  with a set; docstring notes Floyd also works — link module 07).

## Checkpoint
"Hardware diagnostics": `parity_report(packets)` (per-packet bit
counts + overall XOR checksum), `find_faulty_sensor(readings)`
(single-number shape), `firmware_grid_rotate(grid)`,
`prime_channel_ids(limit)` (sieve). Efficiency test on the sieve.

## SUMMARY.md
Cheat-sheet: the bit-recipe table (op → one-liner → what it does),
XOR laws, sieve template, fast-pow reminder, language-reality box
(32-bit vs bigint). Mindmap. Self-quiz 8 Qs. Pattern-recognition
drill: 6 one-liners ("appears once", "O(1) space", "how many
primes", decoys).
