# Handoff: Module 11 — Trees & BSTs

Build `11-trees-bst/`. Read `CONVENTIONS.md` and the master spec
first. You own ONLY this folder.

Audience: completed modules 01–10 (recursion module 08 is the direct
prerequisite; queues from 06 power BFS).

Node convention: ex01 defines `TreeNode` (value, left, right) plus
helpers `tree_from_level_array` (None/null gaps, LeetCode-style) and
`tree_to_level_array` — every later test in the module uses these
helpers to build/inspect trees. Later exercises import from ex01's
file.

## LESSON.md outline
1. Why this exists: hierarchies are everywhere (file systems, DOM,
   org charts); BSTs give O(log n) ordered search that hash maps
   can't (range queries, sorted order).
2. Vocabulary in one table: root/leaf/depth/height/balanced/complete.
3. REQUIRED diagram: one binary tree with the four traversal orders
   listed beside it (pre/in/post/level) — same tree, four orders.
4. DFS recursively: the "trust the subtree" leap of faith (link back
   to module 08); the pre/in/post positions in code.
5. DFS iteratively with an explicit stack; BFS with a queue.
   REQUIRED diagram: BFS frontier expanding level by level.
6. BSTs: the invariant (EVERY left descendant < node < every right
   descendant — not just children; this is the validate trap, flag
   it here); insert/search/min/delete (three delete cases,
   diagrammed).
7. How to recognize it: "per level" → BFS; "path from root" /
   "combine child answers" → DFS; "sorted order from a tree" /
   "range" → inorder/BST.
8. Complexity: O(h); balanced h = log n, degenerate h = n (mention
   that self-balancing exists — AVL/red-black — but is
   out-of-scope detail).
9. Gotchas: validate-with-bounds not with-children, null children
   everywhere, recursion depth on skewed trees.

## Exercises (exactly 8)
- ex01 "build-bst" — `TreeNode` + helpers (see above) + `BST` class:
  `insert/contains/min_value/max_value/to_sorted_array` (inorder).
  Duplicates: ignore (pin it).
- ex02 "bst-delete-validate" — `delete_value(root, v)` (three cases,
  successor swap) and `is_valid_bst(root)` with min/max bounds;
  tests include the famous "child ok, grandchild wrong" tree.
- ex03 "traversals" — free functions `preorder/inorder/postorder`
  (recursive) + `inorder_iterative` (explicit stack) +
  `level_order(root)` → list of levels (BFS).
- ex04 "tree-metrics" — `max_depth`, `count_nodes`, `is_balanced`
  (bottom-up, O(n) — tests punish the naive O(n²) with a big
  skewed tree), `diameter(root)`.
- ex05 "tree-transforms" — `invert(root)`, `is_same_tree(a, b)`,
  `is_subtree(root, sub)`, `is_symmetric(root)`.
- ex06 "bst-tasks" — `kth_smallest(root, k)` (inorder early stop),
  `lca_bst(root, a, b)` (walk from root using ordering),
  `range_sum_bst(root, lo, hi)` (prune subtrees — docstring: this
  is why BST beats hash here).
- ex07 "level-patterns" — `right_side_view(root)`,
  `level_averages(root)`, `zigzag_levels(root)`.
- ex08 "construct-tree" — HARD: `build_from_pre_in(preorder,
  inorder)` reconstruct the tree (index-map optimization required —
  efficiency test on a 10_000-node tree).

## Checkpoint
"Company org chart" (each node: name + up to two reports as
left/right for this exercise) — `headcount(root)`,
`management_depth(root)`, `chain_of_command(root, name)` (root→person
path), `meetings_by_level(root)` (BFS groups), `common_manager(root,
a, b)` (LCA general tree version with the two-value DFS).

## SUMMARY.md
Cheat-sheet: traversal table (order, use-case, iterative tool),
BST op costs (balanced vs skewed), the validate-bounds template,
"which traversal when" decision list. Mindmap. Self-quiz 8 Qs.
Pattern-recognition drill: 8 one-liners (level cues → BFS, path cues
→ DFS, sorted/range cues → BST).
