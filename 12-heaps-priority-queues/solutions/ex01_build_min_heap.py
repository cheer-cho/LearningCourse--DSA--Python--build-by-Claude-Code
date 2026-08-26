class MinHeap:
    def __init__(self) -> None:
        # Pattern: complete binary tree stored flat in a list; index i's
        # children live at 2i+1 / 2i+2, its parent at (i-1)//2.
        # push/pop: O(log n) — sift climbs/descends the tree height.
        self._data: list[int] = []

    def push(self, val: int) -> None:
        self._data.append(val)
        self._sift_up(len(self._data) - 1)

    def pop(self) -> int:
        if not self._data:
            raise IndexError("pop from empty heap")
        top = self._data[0]
        last = self._data.pop()
        if self._data:
            self._data[0] = last
            self._sift_down(0)
        return top

    def peek(self) -> int:
        if not self._data:
            raise IndexError("peek from empty heap")
        return self._data[0]

    def size(self) -> int:
        return len(self._data)

    @classmethod
    def heapify(cls, nums: list[int]) -> "MinHeap":
        # Pattern: bottom-up heapify. Sift down every node with children,
        # last parent -> root. O(n) total: most nodes sit near the leaves
        # and sift almost 0 levels, so the per-node work doesn't grow
        # with log n on average (see LESSON.md for the full argument).
        heap = cls()
        heap._data = list(nums)
        last_parent = (len(heap._data) - 2) // 2
        for i in range(last_parent, -1, -1):
            heap._sift_down(i)
        return heap

    def _sift_up(self, i: int) -> None:
        data = self._data
        while i > 0:
            parent = (i - 1) // 2
            if data[i] >= data[parent]:
                break
            data[i], data[parent] = data[parent], data[i]
            i = parent

    def _sift_down(self, i: int) -> None:
        data = self._data
        n = len(data)
        while True:
            left, right = 2 * i + 1, 2 * i + 2
            smallest = i
            if left < n and data[left] < data[smallest]:
                smallest = left
            if right < n and data[right] < data[smallest]:
                smallest = right
            if smallest == i:
                break
            data[i], data[smallest] = data[smallest], data[i]
            i = smallest
