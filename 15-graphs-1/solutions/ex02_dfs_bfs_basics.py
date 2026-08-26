from collections import deque


def reachable(adj: dict[int, list[int]], start: int) -> set[int]:
    # Pattern: DFS with an explicit stack, visited-on-push.
    # Complexity: O(V + E) time, O(V) space.
    visited = {start}
    stack = [start]
    while stack:
        node = stack.pop()
        for neighbor in adj[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
    return visited


def bfs_order(adj: dict[int, list[int]], start: int) -> list[int]:
    # Pattern: BFS with a queue, visited-on-ENQUEUE (not on dequeue) —
    # the rule that prevents a node being queued twice before either
    # copy is processed.
    # Complexity: O(V + E) time, O(V) space.
    visited = {start}
    order = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in adj[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order


def connected_components(adj: dict[int, list[int]]) -> int:
    # Pattern: loop over every node, BFS/DFS from each unvisited one —
    # each fresh traversal claims exactly one whole component.
    # Complexity: O(V + E) time, O(V) space.
    visited: set[int] = set()
    count = 0
    for node in adj:
        if node in visited:
            continue
        count += 1
        visited.add(node)
        stack = [node]
        while stack:
            current = stack.pop()
            for neighbor in adj[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
    return count


def path_exists(adj: dict[int, list[int]], a: int, b: int) -> bool:
    # Pattern: DFS from a, stop early the moment b is found (or the
    # trivial a == b case).
    # Complexity: O(V + E) time, O(V) space.
    if a == b:
        return True
    visited = {a}
    stack = [a]
    while stack:
        node = stack.pop()
        for neighbor in adj[node]:
            if neighbor == b:
                return True
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
    return False
