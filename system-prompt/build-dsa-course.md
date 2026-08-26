# Build spec: Data Structures & Algorithms course (zero → hero)

Build a complete, self-paced Data Structures & Algorithms course as a
repository the student studies inside VS Code with Claude Code acting as
instructor. This course exists in TWO parallel repositories with an
IDENTICAL curriculum:

- `~/study/Python/DSA-Course-Created-By-Claude/` (Python 3.12+, uv, pytest)
- `~/study/TypeScript/DSA-Course-Created-By-Claude/` (TypeScript 5, vitest)

It uses the same system as the language courses
(`~/study/Python/Course-Created-By-Claude/`,
`~/study/TypeScript/Course-Created-By-Claude/`) — same module anatomy,
same runner scripts, same instructor mode. Reuse their conventions
wherever this spec doesn't say otherwise.

## Goal

Zero → hero in data structures, algorithms, and **interview patterns**:

- every core data structure, **built from scratch** at least once
  (dynamic array, hash map, linked list, stack, queue, BST, heap, trie,
  union-find, segment tree);
- every core algorithm family (sorting, binary search, DFS/BFS,
  backtracking, greedy, dynamic programming, graph algorithms);
- every named interview pattern (two pointers, sliding window, prefix
  sums, fast & slow pointers, monotonic stack, top-K / two heaps,
  intervals, search-on-answer, subsets/permutations, topological sort,
  knapsack, ...);
- and — most importantly — the **thinking process**: how to recognize
  which pattern a new problem belongs to, and how to get from brute
  force to the optimal solution step by step.

Coverage benchmark: NeetCode "DSA for Beginners" + NeetCode "Advanced
Algorithms" + the classic LeetCode interview canon (Blind-75 style).
Exercises are ORIGINAL rewrites of classic problems: same underlying
idea, self-contained statement, our own scenario names — never copied
problem text.

## Pedagogy — the thinking process is the product

Every LESSON.md must follow this flow, per pattern/structure taught:

1. **Why this exists** — the problem it solves, in 2–3 sentences, and
   the naive alternative it beats (with complexities).
2. **Mermaid diagram** of the structure/algorithm in action.
3. **How to recognize it** — a short bulleted list of problem-statement
   cues ("sorted input + pair target → two pointers", "'shortest' on an
   unweighted graph → BFS"). This section is REQUIRED in every lesson.
4. **The template** — minimal skeleton code of the pattern, annotated.
5. **Worked example** — one small input traced step by step (use a
   table or diagram of the state at each step, not prose).
6. **Complexity** — time/space, and one sentence on WHY.
7. **Common gotchas** (off-by-one, empty input, overflow, mutation...).
8. **Try it now** → exercises.

Additional course-wide rules:

- Every exercise docstring/JSDoc states the **target complexity** (e.g.
  "aim for O(n) time, O(1) space"). Reference solutions must meet it
  and include a short comment block: the pattern used, why it applies,
  and the complexity.
- Where feasible, tests enforce efficiency behaviorally (large-input
  tests sized so the naive approach is obviously infeasible — e.g.
  n = 10^5 for an O(n log n) target vs an O(n²) naive; op-counting
  hooks where a comparator/callback is injectable). Never wall-clock
  assertions tighter than generous sanity bounds.
- "From scratch" builds must not use the language's built-in shortcut
  (e.g. building HashMap: no dict/Map for the buckets' core mapping;
  building a heap: no `heapq`).
- Each module's SUMMARY.md ends with a **pattern-recognition drill**:
  5–10 one-line problem descriptions; the student names the
  pattern/structure before peeking at answers in `<details>`.
- Progression within a module: first BUILD the structure (guided),
  then USE it on classic problems, easy → hard.

## Readability & diagrams

Identical to the language courses: short sentences, plain language,
diagram-first, every Mermaid diagram captioned with one italic line
starting "*What to notice:*". Only widely-supported Mermaid types
(flowchart, graph, sequenceDiagram, mindmap). Tables for comparisons
(array vs linked list, BFS vs DFS, memo vs tabulation...).
ROADMAP.md opens with a single Mermaid flowchart of the whole course.

## Repository structure

Mirrors the language courses exactly:

- README.md — overview, setup, how to run tests, study loop.
- ROADMAP.md — course-map flowchart + progress checklist.
- CLAUDE.md — instructor mode (adapted for DSA: includes complexity
  interrogation — "what's the complexity? can you do better?" — and
  mock-interview mode on request).
- NOTES.md, playground/, scripts/, system-prompt/ (this spec +
  handoffs/).
- One folder per module `NN-name/` with LESSON.md, exercises/ (stubs +
  tests), solutions/, checkpoint + its test, SUMMARY.md.

## Curriculum (22 modules, identical in both languages)

**Part I — Foundations & linear structures**
1.  `01-big-o-foundations` — RAM model; time/space complexity; Big-O
    from code; amortized cost (intro); the 5-step problem-solving
    framework (understand → brute force → find the bottleneck → apply a
    pattern → verify) used everywhere afterwards.
2.  `02-arrays-dynamic-arrays` — static vs dynamic arrays; BUILD a
    dynamic array (push/pop/resize, amortized O(1)); in-place
    techniques; string basics.
3.  `03-hashing` — hash map/set usage patterns (counting, complement
    lookup, grouping by key); BUILD a hash map (chaining + resize).
4.  `04-two-pointers-prefix-sums` — opposite-ends & same-direction two
    pointers; prefix sums & range queries.
5.  `05-sliding-window` — fixed-size and variable-size windows;
    window + hash map combos.
6.  `06-stacks-queues` — BUILD stack & queue (incl. queue-via-stacks);
    matching/nesting problems; monotonic stack.
7.  `07-linked-lists` — BUILD singly & doubly linked lists; reversal;
    fast & slow pointers (middle, cycle); merge; LRU cache capstone.
8.  `08-recursion-divide-conquer` — call-tree thinking; base cases;
    recursion ↔ iteration; divide & conquer (fast pow, count
    inversions); memoization taste (full DP later).
9.  `09-sorting` — elementary sorts briefly; merge sort & quick sort
    from scratch; quickselect; bucket/counting sort; stability;
    sorting with comparators as a problem-solving tool.
10. `10-binary-search` — the bug-free template; first/last occurrence;
    rotated arrays; **search on the answer** (min feasible speed/
    capacity); 2D matrix search.

**Part II — Trees, heaps, graphs & combinatorial search**
11. `11-trees-bst` — terminology; BUILD a BST (insert/search/delete/
    validate); DFS traversals (recursive AND iterative) + BFS level
    order; depth/diameter/invert/LCA; tree problem patterns.
12. `12-heaps-priority-queues` — BUILD a binary min-heap (heapify,
    push/pop); heap sort; top-K pattern; k-closest; two-heaps running
    median; merge k sorted lists.
13. `13-tries` — BUILD a trie (insert/search/prefix); wildcard search;
    prefix counting; when a trie beats a hash map.
14. `14-backtracking` — the choose/explore/unchoose template; subsets,
    combinations, permutations; combination sum; word search on a
    grid; palindrome partitioning; N-queens; pruning.
15. `15-graphs-1` — representations (adjacency list/matrix, grid-as-
    graph); DFS & BFS (recursive + iterative); islands & flood fill;
    shortest path on unweighted graphs (multi-source BFS); connected
    components; graph cloning.
16. `16-graphs-2` — topological sort (cycle detection, course
    scheduling); BUILD union-find (rank + path compression) and apps;
    minimum spanning tree (Kruskal + Prim); Dijkstra; Bellman-Ford
    taste (k-stops cheapest path).
17. `17-greedy-intervals` — greedy reasoning & exchange argument
    (informal); Kadane's; jump/reach problems; gas station; interval
    patterns (merge, insert, non-overlapping, meeting rooms).

**Part III — Dynamic programming & beyond**
18. `18-dp-1d` — memoization vs tabulation (framework: state, choice,
    recurrence, base case, order); climbing stairs → house robber (I &
    II) → coin change → word break → decode ways → LIS (O(n²) then
    O(n log n)).
19. `19-dp-2d` — grid paths; longest common subsequence; edit
    distance; 0/1 knapsack; unbounded knapsack (coin change II);
    target sum; palindromic substrings & longest palindromic
    substring (expand-around-center vs DP).
20. `20-bit-manipulation-math` — bit operators & masks; XOR tricks;
    counting bits; reverse bits; power-of-two checks; essential math
    (gcd, fast pow, primes/sieve, matrix traversal/rotation).
21. `21-advanced-structures-strings` — BUILD a segment tree (range
    query + point update) and a Fenwick tree; sliding-window maximum
    (monotonic deque); string matching (Rabin-Karp, KMP); when these
    actually appear in interviews.
22. `22-capstone-interview-sets` — no new theory. Three timed mixed
    sets (easy/medium/hard) spanning all patterns, a pattern-
    recognition final drill, and a coverage map linking every classic
    interview topic back to its module. CLAUDE.md's mock-interview
    mode drives these.

## Technical requirements

- Same toolchains and runner UX as the language courses:
  - Python: uv; `uv run pytest`, `uv run python scripts/test.py NN -k exMM`,
    `uv run python scripts/verify_solutions.py NN`; ruff clean.
  - TypeScript: `npm test -- NN -t exMM`, `npm run verify:solutions -- NN`;
    vitest with typecheck enabled; tsconfig strict.
- Fresh clone: everything imports/compiles cleanly; failing tests are
  the only red, each failure = an unsolved exercise.
- Local Markdown + code only; no services, no internet needed.
- Per-module handoffs live in `system-prompt/handoffs/` (CONVENTIONS.md
  + module-NN.md). Handoff files are LANGUAGE-NEUTRAL and shared by
  both repos; CONVENTIONS.md is per-repo and maps neutral exercise
  slugs to concrete filenames.

## Process

Orchestrator writes scaffold + all handoffs first, then one sub-agent
per module folder (disjoint ownership, deps pre-installed), then the
orchestrator verifies everything (full test run, verify-solutions,
lint/typecheck) before declaring the course done.
