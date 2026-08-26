DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def _flood_fill_area(grid: list[list[int]], visited: set[tuple[int, int]], sr: int, sc: int) -> int:
    """Iterative BFS/DFS flood fill from (sr, sc); returns area claimed."""
    rows, cols = len(grid), len(grid[0])
    visited.add((sr, sc))
    stack = [(sr, sc)]
    area = 0
    while stack:
        r, c = stack.pop()
        area += 1
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr, nc) not in visited:
                visited.add((nr, nc))
                stack.append((nr, nc))
    return area


def count_islands(grid: list[list[int]]) -> int:
    # Pattern: grid-as-graph, iterative flood fill from every unvisited
    # land cell; each flood-fill call claims exactly one whole island.
    # Why iterative: recursive DFS could recurse rows*cols deep on a
    # snake-shaped island, past Python's recursion limit.
    # Complexity: O(rows * cols) time, O(rows * cols) space worst case.
    rows, cols = len(grid), len(grid[0])
    visited: set[tuple[int, int]] = set()
    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                islands += 1
                _flood_fill_area(grid, visited, r, c)
    return islands


def max_island_area(grid: list[list[int]]) -> int:
    # Pattern: same flood fill as count_islands, but track the max area
    # returned instead of just counting flood-fill calls.
    # Complexity: O(rows * cols) time, O(rows * cols) space.
    rows, cols = len(grid), len(grid[0])
    visited: set[tuple[int, int]] = set()
    best = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                best = max(best, _flood_fill_area(grid, visited, r, c))
    return best
