def to_adjacency(n: int, edges: list[tuple[int, int]], directed: bool) -> dict[int, list[int]]:
    # Pattern: adjacency-list construction. Every node gets a key up
    # front (even isolated ones) so later exercises can safely iterate
    # adj.keys() to reach every node, not just endpoints of an edge.
    # Complexity: O(V + E) time/space.
    adj: dict[int, list[int]] = {node: [] for node in range(n)}
    for a, b in edges:
        adj[a].append(b)
        if not directed:
            adj[b].append(a)
    return adj


def degrees(adj: dict[int, list[int]]) -> dict[int, int]:
    # Pattern: single pass counting the length of each neighbor list.
    # Complexity: O(V + E) time, O(V) space.
    return {node: len(neighbors) for node, neighbors in adj.items()}


def matrix_to_list(matrix: list[list[int]]) -> dict[int, list[int]]:
    # Pattern: scan every cell, record a 1 as an edge i -> j.
    # Complexity: O(V^2) time (must inspect every cell), O(V + E) space.
    n = len(matrix)
    adj: dict[int, list[int]] = {node: [] for node in range(n)}
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                adj[i].append(j)
    return adj


def list_to_matrix(adj: dict[int, list[int]], n: int) -> list[list[int]]:
    # Pattern: inverse of matrix_to_list — set matrix[i][j] = 1 for
    # each neighbor j of i.
    # Complexity: O(V^2) time/space (the matrix itself is V^2 cells).
    matrix = [[0] * n for _ in range(n)]
    for node, neighbors in adj.items():
        for neighbor in neighbors:
            matrix[node][neighbor] = 1
    return matrix
