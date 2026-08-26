# Handoff: Module 13 — Tries

Build `13-tries/`. Read `CONVENTIONS.md` and the master spec first.
You own ONLY this folder.

Audience: completed modules 01–12 (trees; hash maps).

## LESSON.md outline
1. Why this exists: a hash map answers "is this exact word here?";
   it cannot answer "what starts with 'pre'?" without scanning
   everything. A trie shares prefixes structurally.
2. REQUIRED diagram: trie containing ["car", "card", "care", "dog"]
   — shared c-a-r spine, end-of-word markers highlighted.
3. Anatomy: node = children map + is_end flag (children as hash map;
   mention the fixed-26-array alternative and its trade-off).
4. Operations: insert / exact search / starts_with, all O(L) in word
   length — independent of how many words are stored (the headline).
5. How to recognize it: "prefix", "autocomplete", "starts with",
   "many words + character-by-character matching", "wildcard over a
   dictionary".
6. Worked example: insert "care" after "car" traced node by node.
7. Wildcard search = DFS branching at '.' — small flowchart
   (REQUIRED diagram can be this or #2's plus one more; two total
   minimum).
8. Gotchas: is_end vs has-children confusion ("car" vs "card"),
   counting words vs counting nodes, memory footprint honesty.

## Exercises (exactly 5)
- ex01 "build-trie" — BUILD `Trie`: `insert(word)`, `search(word)`
  (exact), `starts_with(prefix)`. Node class with children map +
  end flag. Tests: "car"/"card" independence, empty string policy
  (pin: empty prefix → True, empty word insert allowed).
- ex02 "wildcard-dictionary" — `WordDictionary`: `add_word(word)`,
  `search(pattern)` where '.' matches any single char (DFS). Tests
  include all-dots, no-match-by-length.
- ex03 "prefix-counts" — extend the trie idea: each node stores a
  pass-through counter; `PrefixCounter`: `insert(word)`,
  `count_starting_with(prefix)` O(prefix length), plus
  `autocomplete(prefix, k)` → up to k completions in alphabetical
  order (DFS in sorted child order). Efficiency test: 10_000 words,
  many queries.
- ex04 "replace-roots" — `replace_with_roots(roots, sentence)`:
  replace each word by its SHORTEST root from the dictionary if one
  exists (classic "successor" problem, fresh scenario: abbreviation
  expansion). Build trie of roots, walk each word to first end
  marker.
- ex05 "unique-prefixes" — `shortest_unique_prefix(words)` → for
  each word its shortest prefix shared with no other word (counter
  nodes); `longest_common_prefix_all(words)` via the trie spine.
  Docstring compares against the sort-based LCP alternative.

## Checkpoint
"Search-box engine": `SearchBox` combining it all —
`index(word)`, `suggest(prefix, k)` (top-k alphabetical),
`match(pattern)` ('.'-wildcard), `popularity(prefix)` (count of
indexed words under prefix). Efficiency test: 20_000 words indexed,
1_000 mixed queries.

## SUMMARY.md
Cheat-sheet: node anatomy, op costs in terms of L vs n, trie vs hash
map vs sorted-array comparison TABLE (exact lookup / prefix query /
memory), wildcard-DFS template. Mindmap. Self-quiz 6 Qs.
Pattern-recognition drill: 6 one-liners (prefix cues vs exact-lookup
decoys → hash map).
