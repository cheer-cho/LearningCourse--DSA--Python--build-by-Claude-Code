# Course-Wide Conventions — Python DSA course (read this first)

You are one of several agents building a self-paced Data Structures &
Algorithms course. The master spec is `../build-dsa-course.md` — read it
fully, especially the **Pedagogy** section: the thinking process
(pattern recognition, brute force → optimal) is the product.

Style reference: `/home/acheer/study/Python/Course-Created-By-Claude/`
— e.g. `04-collections/LESSON.md` and its exercises. Match that tone:
short sentences, diagram-first, encouraging, no walls of text.

## Repo root
`/home/acheer/study/Python/DSA-Course-Created-By-Claude/`

## Toolchain
- Python 3.12+, managed with `uv` (deps already installed).
- Run everything through uv: `uv run pytest`, `uv run python ...`.
- Standard library only. `heapq`/`bisect`/`collections` are ALLOWED in
  problem-solving exercises but FORBIDDEN inside the "build it from
  scratch" exercises they would trivialize (the handoff marks these).

## Module folder anatomy
```
NN-module-name/
  LESSON.md            # follows the 8-step flow in the master spec
  exercises/
    exNN_slug.py       # stub the student edits
    test_exNN_slug.py  # pytest tests for it
  solutions/
    exNN_slug.py       # reference solution (same filename as stub)
    checkpoint_NN.py   # reference solution for the checkpoint
  checkpoint_NN.py     # graded checkpoint stub (module root)
  test_checkpoint_NN.py
  SUMMARY.md           # cheat-sheet + mindmap + self-quiz
                       #  + pattern-recognition drill (spec requires it)
```

## Naming — IMPORTANT (import-collision rule)
Handoffs name exercises with neutral slugs like `ex03 "pair-sum"`.
Concrete filename here: `ex03_pair_sum.py` (slug → snake_case). Every
importable filename must be unique across the WHOLE course; the handoff
slugs guarantee this — never rename or merge exercises. Checkpoints:
`checkpoint_NN.py`. The root `conftest.py` puts every module dir and
`exercises/` dir on `sys.path`; tests import naturally:
`from ex03_pair_sum import pair_sum`.

## Exercise file rules
- File header comment: 2–4 lines — scenario, pattern(s) covered, exact
  test command. Never a numbered spec.
- Each function/class carries a plain-English docstring: what it does,
  params, return, edge cases, 1–3 `input -> output` examples, and a
  **Target complexity:** line (e.g. `Target: O(n) time, O(1) space`).
- Stub bodies: `raise NotImplementedError` after the docstring. For
  class-based builds, stub every method that way.
- Every stub file must import cleanly on a fresh clone. Failing tests
  are the ONLY intended red.
- Difficulty progresses ex01 → exNN: build/guided first, then classic
  problems easy → hard.
- Type hints on all signatures (modern syntax: `list[int]`, `X | None`).

## Test file rules
- pytest, plain `assert`, descriptive names
  (`def test_pair_sum_handles_negatives():`).
- Import at module top: `from ex03_pair_sum import pair_sum`.
- Several small tests per exercise: happy path, edge cases (empty,
  single element, duplicates, negatives, already-sorted, all-equal...).
- Where the handoff says "efficiency test": include one large-input
  test (build the input programmatically) sized so the naive approach
  is infeasible but the target complexity passes instantly. Never
  tight wall-clock assertions.
- Tests must be red against the stub, green against the solution.
- Use `pytest.raises` for error specs; `pytest.approx` for floats.

## Solution file rules
- Must meet the stated target complexity.
- Top-of-function comment block: pattern used, why it applies here,
  time/space complexity. Keep it 3–6 lines.

## Commands (already wired — do not redefine)
- `uv run pytest` — everything
- `uv run pytest 05-sliding-window` — one module
- `uv run python scripts/test.py 5 -k ex02` — one exercise
- `uv run python scripts/verify_solutions.py 05` — module's tests
  against reference solutions (must exit 0)

## Mermaid rules
- Every LESSON.md: at least 2 diagrams (structure/algorithm state
  diagrams are ideal); every SUMMARY.md: exactly one `mindmap`. Every
  diagram gets a one-line italic caption starting "*What to notice:*".
- Only widely-supported syntax (flowchart TD/LR, graph, sequenceDiagram,
  mindmap). Quote node labels with special characters.

## Definition of done for a module (verify ALL before finishing)
1. `uv run python -m compileall <module-dir>` — clean.
2. `uv run pytest <module-dir>` — collects cleanly; every failure is an
   unsolved exercise, never an import/collection error.
3. `uv run python scripts/verify_solutions.py <NN>` — exits 0.
4. `uv run ruff check <module-dir>` — clean.
5. LESSON.md follows the 8-step flow (incl. "How to recognize it");
   SUMMARY.md has the pattern-recognition drill.
6. You did NOT edit any file outside your module folder.

Report back (final message): module name, exercise list (one line
each), verification outputs summarized, any convention you had to bend
(should be none).
