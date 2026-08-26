from __future__ import annotations

from ex01_build_bst import TreeNode


def build_from_pre_in(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    # Pattern: preorder[0] is always the current subtree's root; its
    # position in inorder splits the remaining values into left/right
    # subtrees. A value -> index map (built once) replaces repeated
    # `inorder.index(...)` calls, and passing index bounds replaces
    # slicing — both are what take this from O(n^2) to O(n) time.
    index_of = {value: i for i, value in enumerate(inorder)}
    pre_pos = 0

    def build(in_lo: int, in_hi: int) -> TreeNode | None:
        nonlocal pre_pos
        if in_lo > in_hi:
            return None
        root_value = preorder[pre_pos]
        pre_pos += 1
        root = TreeNode(root_value)
        mid = index_of[root_value]
        root.left = build(in_lo, mid - 1)
        root.right = build(mid + 1, in_hi)
        return root

    return build(0, len(inorder) - 1)
