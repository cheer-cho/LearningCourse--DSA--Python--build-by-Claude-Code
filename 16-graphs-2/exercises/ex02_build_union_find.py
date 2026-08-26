# Scenario: a social network's "friend circles" -- accounts merge into
# one circle whenever a friendship forms, and you need instant
# "same circle?" answers as friendships keep arriving.
# Pattern: BUILD a union-find (disjoint set union) from scratch --
# parent forest + path compression + union by rank.
# Run: uv run pytest 16-graphs-2 -k ex02


class UnionFind:
    """Disjoint-set-union over elements `0..n-1`.

    Internally a forest: each element points at a `parent`, and the
    root of a tree is its own parent. Two elements are "connected" iff
    they share a root. `find` uses path compression (every node on the
    path gets re-parented straight to the root) and `union` attaches
    the smaller/shallower tree under the larger/deeper one (union by
    rank) -- together these keep every operation near O(1) amortized,
    instead of the O(n) worst case a naive linked-list-style union
    would allow.

    Target: O(n) time, O(n) space to build; every method below is
    O(alpha(n)) amortized (alpha = inverse Ackermann, effectively a
    small constant for any n you'll ever encounter).
    """

    def __init__(self, n: int) -> None:
        """Create `n` singleton sets: element `i` starts as its own
        root, in a set of size 1.

        Target: O(n) time, O(n) space.
        """
        raise NotImplementedError

    def find(self, x: int) -> int:
        """Return the root of the set containing `x`, compressing the
        path so every visited node points directly at the root
        afterward (path compression).

        Target: O(alpha(n)) amortized time.
        """
        raise NotImplementedError

    def union(self, x: int, y: int) -> bool:
        """Merge the sets containing `x` and `y`. Attach the
        lower-rank root under the higher-rank root (union by rank); on
        a tie, either direction works but bump the surviving root's
        rank by 1. Return True if a merge happened, False if `x` and
        `y` were already in the same set (nothing to do).

        Target: O(alpha(n)) amortized time.
        """
        raise NotImplementedError

    def connected(self, x: int, y: int) -> bool:
        """Return True if `x` and `y` are currently in the same set.

        Target: O(alpha(n)) amortized time.
        """
        raise NotImplementedError

    def component_count(self) -> int:
        """Return the current number of disjoint sets (starts at `n`,
        decreases by 1 on every successful `union`).

        Target: O(1) time -- track a running counter, don't recompute.
        """
        raise NotImplementedError
