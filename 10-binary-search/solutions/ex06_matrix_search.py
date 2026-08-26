def search_matrix(grid: list[list[int]], target: int) -> bool:
    # Pattern: THE template over a flattened index space. grid[i][0] >
    # grid[i-1][-1] for every row means flat index i -> grid[i // n][i
    # % n] is a single sorted sequence -- one binary search, no need to
    # search each row separately.
    # Time: O(log(m * n)). Space: O(1).
    m = len(grid)
    n = len(grid[0])
    lo, hi = 0, m * n
    while lo < hi:
        mid = lo + (hi - lo) // 2
        value = grid[mid // n][mid % n]
        if value < target:
            lo = mid + 1
        else:
            hi = mid
    return lo < m * n and grid[lo // n][lo % n] == target
