from collections import deque


def build_order(n: int, prereqs: list[tuple[int, int]]) -> list[int] | None:
    # Pattern: Kahn's algorithm -- in-degree array + queue of
    # zero-in-degree nodes. Why: peeling off "ready" nodes (no
    # unfinished prereqs) and decrementing their neighbors' in-degree
    # is exactly BFS layer-by-layer over a DAG; a leftover in-degree
    # after the queue drains means a cycle blocked those nodes forever.
    # Complexity: O(n + e) time/space.
    graph: list[list[int]] = [[] for _ in range(n)]
    in_degree = [0] * n
    for course, prereq in prereqs:
        graph[prereq].append(course)
        in_degree[course] += 1

    queue: deque[int] = deque(node for node in range(n) if in_degree[node] == 0)
    order: list[int] = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == n else None


def can_finish(n: int, prereqs: list[tuple[int, int]]) -> bool:
    # Pattern: cycle detection is topological sort's free side effect --
    # a valid order exists iff there's no cycle.
    # Complexity: O(n + e) time/space.
    return build_order(n, prereqs) is not None
