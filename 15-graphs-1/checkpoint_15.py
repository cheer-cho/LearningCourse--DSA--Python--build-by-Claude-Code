# Checkpoint 15 — Social graph
#
# A social network is a friendship edge list over users 0..n-1
# (undirected: friendship goes both ways). Build four tools, each
# reusing a traversal pattern from this module:
#   - friend_circles: connected components (ex02)
#   - degrees_of_separation: BFS shortest-path distance (ex05)
#   - suggested_friends: BFS one level out, set difference
#   - can_two_team: bipartite check via BFS 2-coloring (ex07)
#
# Run: uv run pytest 15-graphs-1 -k checkpoint_15


def friend_circles(edges: list[tuple[int, int]], n: int) -> int:
    """Users are `0..n-1`; `edges` is a list of undirected friendship
    pairs. Return the number of "friend circles" — connected
    components of the friendship graph. A user with no friends is
    their own circle of one.

    friend_circles([(0, 1), (1, 2), (3, 4)], 5) -> 2
        (circle {0, 1, 2}, circle {3, 4})
    friend_circles([], 3) -> 3   (everyone is their own circle)

    Target: O(n + E) time, O(n) space.
    """
    raise NotImplementedError


def degrees_of_separation(edges: list[tuple[int, int]], a: int, b: int) -> int:
    """Return the fewest friendship hops connecting user `a` to user
    `b` (BFS shortest-path distance on the undirected friendship
    graph), or `-1` if they're not connected at all. `a == b` is
    always `0`.

    degrees_of_separation([(0, 1), (1, 2), (2, 3)], 0, 3) -> 3
    degrees_of_separation([(0, 1), (2, 3)], 0, 3) -> -1
    degrees_of_separation([(0, 1)], 0, 0) -> 0

    Target: O(n + E) time, O(n) space.
    """
    raise NotImplementedError


def suggested_friends(edges: list[tuple[int, int]], user: int) -> list[int]:
    """"People you may know": every user who is a friend-of-a-friend
    of `user` but NOT already a direct friend and not `user`
    themself. Return the result sorted ascending, with no duplicates.

    suggested_friends([(0, 1), (1, 2), (1, 3), (2, 3)], 0) -> [2, 3]
        (0's only friend is 1; 1's friends are 0, 2, 3; remove 0 itself
        and 0's existing friend 1 -> [2, 3]. Note 2 and 3 are ALSO
        directly connected to each other, but that doesn't matter —
        only whether they're directly connected to `user`.)
    suggested_friends([(0, 1)], 0) -> []   (1 is a direct friend already)
    suggested_friends([], 5) -> []   (no friends means no friends-of-friends)

    Target: O(n + E) time, O(n) space.
    """
    raise NotImplementedError


def can_two_team(edges: list[tuple[int, int]], n: int) -> bool:
    """Return True if users `0..n-1` can be split into two teams such
    that no two DIRECT friends (an edge) end up on the same team —
    i.e. the friendship graph is bipartite. Disconnected users/groups
    are fine; every group must individually be splittable.

    can_two_team([(0, 1), (1, 2)], 3) -> True
    can_two_team([(0, 1), (1, 2), (2, 0)], 3) -> False   (triangle)

    Target: O(n + E) time, O(n) space.
    """
    raise NotImplementedError
