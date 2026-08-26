from collections import deque

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def minutes_to_infect(grid: list[list[int]]) -> int:
    # Pattern: multi-source BFS. Seed the queue with every infected
    # cell at distance 0 up front — the wavefronts from each source
    # merge automatically because BFS processes strictly by distance.
    # Complexity: O(rows * cols) time, O(rows * cols) space.
    rows, cols = len(grid), len(grid[0])
    queue: deque[tuple[int, int, int]] = deque()
    healthy_remaining = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))
            elif grid[r][c] == 1:
                healthy_remaining += 1

    if healthy_remaining == 0:
        return 0

    minutes = 0
    while queue:
        r, c, minute = queue.popleft()
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                healthy_remaining -= 1
                minutes = minute + 1
                queue.append((nr, nc, minute + 1))

    return minutes if healthy_remaining == 0 else -1


def shortest_exit(maze: list[list[int]], start: tuple[int, int]) -> int:
    # Pattern: single-source BFS distance; stop the moment a border
    # (open) cell is dequeued — BFS guarantees that's the SHORTEST
    # such cell, since it processes strictly by increasing distance.
    # Complexity: O(rows * cols) time, O(rows * cols) space.
    rows, cols = len(maze), len(maze[0])

    def is_border(r: int, c: int) -> bool:
        return r == 0 or r == rows - 1 or c == 0 or c == cols - 1

    sr, sc = start
    if is_border(sr, sc):
        return 0

    visited = {start}
    queue: deque[tuple[int, int, int]] = deque([(sr, sc, 0)])
    while queue:
        r, c, dist = queue.popleft()
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0 and (nr, nc) not in visited:
                if is_border(nr, nc):
                    return dist + 1
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))

    return -1
