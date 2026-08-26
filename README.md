# Data Structures & Algorithms — Python Edition

A self-paced, hands-on DSA course: from "what is Big-O?" to hard
interview problems. You learn by making tests pass, not by reading
long documents. Study it in VS Code with Claude Code as your
instructor (it reads `CLAUDE.md` and coaches you — Socratic hints,
never spoilers).

A twin course with the identical curriculum exists in TypeScript at
`~/study/TypeScript/DSA-Course-Created-By-Claude/`.

## What you'll master

- Every core data structure — most of them **built from scratch**
  (dynamic array, hash map, linked lists, stack, queue, BST, heap,
  trie, union-find, segment tree, Fenwick tree).
- Every interview pattern: two pointers, sliding window, prefix sums,
  monotonic stack, fast & slow pointers, top-K, backtracking, BFS/DFS,
  topological sort, Dijkstra, greedy, intervals, 1-D/2-D DP, bits,
  KMP/Rabin-Karp — and, above all, **how to recognize which one a new
  problem needs**.

## Setup

1. Install [uv](https://docs.astral.sh/uv/) (or use `python -m venv`
   + `pip install pytest ruff` as a fallback).
2. `uv sync` in this folder — that's it.
3. VS Code: install the Python extension. For diagrams, enable
   Markdown preview (built in) — Mermaid renders via the "Markdown
   Preview Mermaid Support" extension.

## The study loop

1. Open the next module's `LESSON.md` (short, diagram-first).
2. Work through `exercises/` in order — each file says how to run
   its tests at the top. Red → your turn; green → done.
3. Stuck? Ask your instructor for a hint (it escalates gently and
   never spoils). Solutions live in `solutions/` — look only when
   you've truly decided to.
4. Finish with the module checkpoint, then skim `SUMMARY.md` and do
   its self-quiz + pattern-recognition drill.
5. Tick your progress in `ROADMAP.md` (the instructor does this for
   you when checkpoints pass).

## Commands

| What | Command |
| --- | --- |
| Everything | `uv run pytest` |
| One module | `uv run python scripts/test.py 5` |
| One exercise | `uv run python scripts/test.py 5 -k ex03` |
| A checkpoint | `uv run python scripts/test.py 5 -k checkpoint` |
| Scratch file | `uv run python playground/idea.py` |
| Maintenance: verify reference solutions | `uv run python scripts/verify_solutions.py 05` |

On a fresh clone **every exercise test fails on purpose** — each red
test is an exercise waiting for you. Nothing should error on import.

## Layout

```
NN-module-name/
  LESSON.md          # the concept, diagram-first
  exercises/         # your work: exNN_slug.py + its tests
  solutions/         # reference solutions — no peeking
  checkpoint_NN.py   # graded module finale (+ its test file)
  SUMMARY.md         # cheat-sheet, mindmap, quiz, pattern drill
```

Start with `ROADMAP.md` to see the whole path, then open
`01-big-o-foundations/LESSON.md`. Good luck — and think in patterns.
