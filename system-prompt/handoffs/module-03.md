# Handoff: Module 03 — Hashing

Build `03-hashing/`. Read `CONVENTIONS.md` and the master spec first.
You own ONLY this folder.

Audience: completed modules 01–02 (Big-O, arrays). This module turns
"can I trade space for time?" into a reflex.

## LESSON.md outline
1. Why this exists: searching an array is O(n); a hash table makes
   lookup O(1) average. Half of all interview optimizations are "throw
   a hash map at it".
2. REQUIRED diagram: graph of key → hash function → bucket index →
   chained entries (show a collision landing in the same bucket).
3. How it works: hash function, buckets, collisions, chaining, load
   factor, resize. Why worst case is O(n) but average O(1).
4. How to recognize it: "have I seen this before?", "count
   occurrences", "find the complement", "group things that share a
   key" → hash map/set.
5. Templates: counting (`counts[k] = counts.get(k, 0) + 1`),
   complement lookup (the two-sum shape), grouping
   (`groups[canonical(x)].append(x)`).
6. Worked example: two-sum traced in a table (index, value, needed,
   map contents).
7. Complexity + what makes a bad key (mutable keys, floats).
8. Gotchas: iteration order assumptions, hashing mutables,
   colliding canonical forms.

## Exercises (exactly 6)
Usage first (ex01–ex04), then build the structure (ex05–ex06).

- ex01 "first-unique" — `first_unique_index(s)` → index of first
  non-repeating character (−1 if none), two-pass counting;
  `majority_item(nums)` → element appearing > n/2 times (counting
  version; mention Boyer-Moore in a comment as a bonus).
- ex02 "pair-sum" — the classic: `pair_sum(nums, target)` → the two
  INDICES (any order) or None/null; one pass with complement map.
  Efficiency test n = 200_000. Docstring contrasts with module 01's
  brute-force `target-pair`.
- ex03 "group-anagrams" — `group_anagrams(words)` → groups of words
  sharing a canonical form (sorted-letters key or 26-count key —
  lesson mentions both; either accepted). Also
  `is_anagram(a, b)`. Tests are order-insensitive across groups.
- ex04 "consecutive-run" — `longest_consecutive(nums)` → length of the
  longest run of consecutive integers, O(n) via set + only start at
  run-beginnings (x-1 not in set). Efficiency test n = 200_000
  (shuffled range chunks). This is THE "set trick" showcase.
- ex05 "window-duplicates" — `has_nearby_duplicate(nums, k)` → any
  equal pair within index distance k (last-seen-index map);
  `first_repeated_within(stream, k)` variant returning the value.
  Bridges toward sliding window (module 05).
- ex06 "build-hash-map" — BUILD `HashMap`: array of buckets, each a
  list of (key, value) pairs; `set/get/delete/size/keys`; resize at
  load factor 0.75 (rehash everything); string and integer keys (a
  simple polynomial string hash — provide the formula in the
  docstring). FROM SCRATCH: no dict/Map/object-as-map for the bucket
  mapping (a plain list/array of lists is the storage). Tests: 10_000
  mixed ops, delete semantics, resize actually happened (expose
  `bucket_count()`).

## Checkpoint
"Log analytics": given a list of (user, action) event pairs —
`action_counts(events)`, `first_unique_user(events)`,
`users_by_action(events)` (grouping), `has_duplicate_burst(events, k)`
(same user+action within k events). All O(n)-ish with hash maps;
efficiency test on 100_000 events.

## SUMMARY.md
Cheat-sheet: the three templates (count / complement / group), hash map
op-cost table (average vs worst), when a set beats a map, load-factor
rule. Mindmap. Self-quiz 8 Qs. Pattern-recognition drill: 8 one-liners
(mix of hash-map cues and deliberate non-hash cues like "sorted input
pair search" → future two pointers).
