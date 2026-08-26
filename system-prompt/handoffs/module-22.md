# Handoff: Module 22 — Capstone: Interview Sets

Build `22-capstone-interview-sets/`. Read `CONVENTIONS.md` and the
master spec first. You own ONLY this folder.

Audience: completed ALL of modules 01–21. NO new theory. This module
is rehearsal: mixed problems with no module label telling you which
pattern applies — exactly like a real interview.

DESIGN RULE: every problem here must be a FRESH scenario (invent
original wrappings) and must NOT duplicate any earlier exercise's
exact problem, but each must map cleanly onto one or two patterns
from modules 01–21. Spread coverage: across the whole module, at
least 12 distinct patterns must appear. In each SOLUTION file, the
comment block must name the pattern and the module it came from —
in the STUBS, never hint at the pattern (that's the point).

## LESSON.md outline
1. Why this exists: knowing 20 patterns is not the skill; picking
   the right one under time pressure is.
2. How to run a set: timebox (easy 15 min, medium 25, hard 40);
   for each problem, WRITE DOWN before coding: restated problem,
   brute force + its complexity, the pattern you suspect and the
   cue that made you suspect it. Only then code.
3. REQUIRED diagram: flowchart of the interview loop (restate →
   examples → brute force → optimize via pattern cues → code →
   trace a test → state complexity).
4. REQUIRED diagram / centerpiece: the CUE MAP — a big flowchart or
   table from problem-statement cues to patterns ("sorted + pair →
   two pointers; contiguous best → window/Kadane; count ways →
   DP; all configurations → backtracking; prereq order → topo;
   updates + range queries → segment tree; ...") covering every
   Part I–III pattern. This is the course's single most valuable
   page — invest in it.
5. Mock-interview mode: how to ask the instructor (Claude) to run
   one (it plays interviewer, gives one hint per problem max,
   asks for complexity at the end — mirrors CLAUDE.md).
6. After each set: score honestly (solved clean / solved with
   hints / stuck), log stuck-reasons in NOTES.md, revisit the
   weak module.

## Exercises (exactly 4)
- ex01 "set-easy" — 6 EASY problems, one function each, fresh
  scenarios over: hash counting, two pointers, fixed window, stack
  matching, BFS on a grid, binary search boundary. Target ~15 min
  each.
- ex02 "set-medium" — 6 MEDIUM problems over: variable window +
  map, monotonic stack, heap top-k, topological sort, 1-D DP,
  backtracking generation. Target ~25 min each. Efficiency tests
  where the pattern is the only way to pass.
- ex03 "set-hard" — 4 HARD problems over: 2-D DP (two-sequence or
  knapsack), Dijkstra or k-stops variant, two-heaps or
  merge-k-sorted, min-cover-window or KMP-style string. Target
  ~40 min each. Efficiency tests mandatory.
- ex04 "pattern-quiz" — 20 one-line problem descriptions in
  comments; student fills a returned dict/record mapping q1..q20 →
  pattern name from a FIXED provided list of labels (the same
  labels as the cue map). Tests assert exact answers. Cover every
  major pattern at least once.

## Checkpoint
"final-mock" — a 4-problem set (1 easy, 2 medium, 1 hard, fresh
scenarios, patterns NOT overlapping ex01–ex03's specific picks
where feasible). Passing this = passing the course. Its test file
header says exactly that in one celebratory line.

## SUMMARY.md
This one is special: the COURSE coverage map — a table of every
interview topic (the NeetCode beginner + advanced canon) → which
module taught it → which exercises drilled it. Plus the cue map
condensed to a table, and a "what next" section (keep a problem
journal, spaced repetition via NOTES.md, harder platforms).
Mindmap of the whole course. Self-quiz: 10 mixed questions from
across all modules. Pattern-recognition drill: 10 one-liners, the
hardest disambiguations in the course (window vs prefix+hash,
greedy vs DP, Dijkstra vs BFS, backtracking vs DP).
