from collections import deque


def is_bipartite(adj: dict[int, list[int]]) -> bool:
    # Pattern: BFS 2-coloring, one traversal per unvisited component
    # (a disconnected graph is bipartite only if every component is).
    # Complexity: O(V + E) time, O(V) space.
    color: dict[int, int] = {}

    for start in adj:
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
