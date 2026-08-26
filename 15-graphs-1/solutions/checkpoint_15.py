from collections import deque


def _build_adjacency(edges: list[tuple[int, int]], n: int) -> dict[int, list[int]]:
    adj: dict[int, list[int]] = {node: [] for node in range(n)}
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    return adj


def friend_circles(edges: list[tuple[int, int]], n: int) -> int:
    # Pattern: connected components (ex02) over the friendship graph.
    # Complexity: O(n + E) time, O(n) space.
    adj = _build_adjacency(edges, n)
    visited: set[int] = set()
    circles = 0
    for start in range(n):
        if start in visited:
            continue
        circles += 1
        visited.add(start)
        stack = [start]
        while stack:
            node = stack.pop()
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
    return circles


def degrees_of_separation(edges: list[tuple[int, int]], a: int, b: int) -> int:
    # Pattern: single-source BFS distance — BFS guarantees the first
    # time b is reached is via a shortest path.
    # Complexity: O(n + E) time, O(n) space.
    if a == b:
        return 0
    adj: dict[int, list[int]] = {}
    for x, y in edges:
        adj.setdefault(x, []).append(y)
        adj.setdefault(y, []).append(x)
    visited = {a}
    queue: deque[tuple[int, int]] = deque([(a, 0)])
    while queue:
        node, dist = queue.popleft()
        for neighbor in adj.get(node, []):
            if neighbor == b:
                return dist + 1
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
    return -1


def suggested_friends(edges: list[tuple[int, int]], user: int) -> list[int]:
    # Pattern: one BFS layer past direct friends, then set difference.
    # Complexity: O(n + E) time, O(n) space.
    adj: dict[int, list[int]] = {}
    for a, b in edges:
        adj.setdefault(a, []).append(b)
        adj.setdefault(b, []).append(a)

    direct = set(adj.get(user, []))
    fof: set[int] = set()
    for friend in direct:
        fof.update(adj.get(friend, []))
    fof.discard(user)
    fof -= direct
    return sorted(fof)


def can_two_team(edges: list[tuple[int, int]], n: int) -> bool:
    # Pattern: BFS 2-coloring (ex07), one traversal per unvisited group.
    # Complexity: O(n + E) time, O(n) space.
    adj = _build_adjacency(edges, n)
    color: dict[int, int] = {}
    for start in range(n):
        if start in color:
            continue
        color[start] = 0
        queue = deque([start])
        while queue:
            node = queue.popleft()
            for neighbor in adj[node]:
                if neighbor not in color:
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
    return True
