# Scenario: reorder a chain in place into a zig-zag from both ends —
# L0, Ln, L1, Ln-1, ... Combines three earlier moves into one plan.
# Concepts: find-the-middle + in-place reversal + interleaving.
# Run: uv run pytest 07-linked-lists -k ex05

from __future__ import annotations

from ex01_build_singly_list import ListNode


def reorder(head: ListNode | None) -> None:
    """Reorder a list in place: L0, L1, ..., Ln becomes
    L0, Ln, L1, L(n-1), L2, L(n-2), ...

    Mutates the chain reachable from `head`; returns nothing (`head`
    itself stays the first node, its `.next` chain is what changes).
    Plan — do each step with a tool you already built this module:
      1. Find the middle (ex03's approach) and split the list in two.
      2. Reverse the second half (ex02's approach).
      3. Interleave the two halves node by node.

    head built from [1, 2, 3, 4]; after reorder(head), head reads [1, 4, 2, 3]
    head built from [1, 2, 3, 4, 5]; after reorder(head), head reads [1, 5, 2, 4, 3]
    reorder(None) -> None (nothing to do)

    Target: O(n) time, O(1) space.
    """
    raise NotImplementedError
