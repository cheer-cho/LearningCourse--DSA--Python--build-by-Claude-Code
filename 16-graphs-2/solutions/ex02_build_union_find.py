class UnionFind:
    # Pattern: disjoint-set-union, built from scratch -- a parent
    # array forest with path compression (find) and union by rank.
    # Why: path compression flattens trees toward the root every time
    # they're visited; union by rank keeps trees shallow by always
    # hanging the smaller tree under the bigger one. Neither alone
    # bounds the height well; together they give near-O(1) ops.
    # Complexity: O(n) build, O(alpha(n)) amortized per operation.

    def __init__(self, n: int) -> None:
        self._parent = list(range(n))
        self._rank = [0] * n
        self._count = n

    def find(self, x: int) -> int:
        root = x
        while self._parent[root] != root:
            root = self._parent[root]
        # Path compression: re-point every node on the path straight
        # at the root, so future finds through them are O(1).
        while self._parent[x] != root:
            self._parent[x], x = root, self._parent[x]
        return root

    def union(self, x: int, y: int) -> bool:
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False

        if self._rank[root_x] < self._rank[root_y]:
            root_x, root_y = root_y, root_x
        self._parent[root_y] = root_x
        if self._rank[root_x] == self._rank[root_y]:
            self._rank[root_x] += 1

        self._count -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def component_count(self) -> int:
        return self._count
