class EditorHistory:
    # Pattern: two stacks of full-document snapshots. undo_stack holds
    # states to revert to; redo_stack holds states an undo stepped away
    # from. A fresh edit clears redo_stack — you can't redo into a
    # future erased by a new branch of typing.
    # Complexity: O(1) time per call, O(k) space for k edits recorded.

    def __init__(self) -> None:
        self.text = ""
        self._undo_stack: list[str] = []
        self._redo_stack: list[str] = []

    def type(self, text: str) -> None:
        self._undo_stack.append(self.text)
        self.text += text
        self._redo_stack.clear()

    def delete_last(self) -> None:
        if not self.text:
            return
        self._undo_stack.append(self.text)
        self.text = self.text[:-1]
        self._redo_stack.clear()

    def undo(self) -> None:
        if not self._undo_stack:
            return
        self._redo_stack.append(self.text)
        self.text = self._undo_stack.pop()

    def redo(self) -> None:
        if not self._redo_stack:
            return
        self._undo_stack.append(self.text)
        self.text = self._redo_stack.pop()


def spans(prices: list[int]) -> list[int]:
    # Pattern: monotonic non-increasing stack of (index, price) pairs —
    # for each day, pop every earlier day whose price is <= today's; the
    # first survivor (or -1) marks the left edge of today's span. Same
    # "each element pushed and popped once" argument as days_until_warmer.
    # Complexity: O(n) time, O(n) space.
    result = [0] * len(prices)
    stack: list[tuple[int, int]] = []
    for i, price in enumerate(prices):
        while stack and stack[-1][1] <= price:
            stack.pop()
        prev_index = stack[-1][0] if stack else -1
        result[i] = i - prev_index
        stack.append((i, price))
    return result
