MAX_TOTAL_COST_PER_APPEND = 3


def append_costs(n: int) -> list[int]:
    # Pattern: simulate a doubling dynamic array. Most appends cost 1;
    # a resize costs (elements copied) + 1, and resizes get
    # exponentially rarer as size grows. O(n) time, O(n) space.
    capacity = 1
    costs = []
    for size in range(n):
        if size == capacity:
            capacity *= 2
            cost = size + 1
        else:
            cost = 1
        costs.append(cost)
    return costs


def total_cost(n: int) -> int:
    # Pattern: sum the simulated costs. O(n) time, O(n) space (reuses
    # append_costs, which allocates the O(n) cost list).
    return sum(append_costs(n))
