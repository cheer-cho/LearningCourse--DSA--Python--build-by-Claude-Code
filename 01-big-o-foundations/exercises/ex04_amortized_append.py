# Scenario: simulate a doubling dynamic array (the one you'll build for
# real in module 02) and prove, with numbers, that its average append
# cost stays O(1) even though individual appends spike.
# Concepts: amortized cost, doubling strategy.
# Run: uv run pytest 01-big-o-foundations -k ex04

MAX_TOTAL_COST_PER_APPEND = 3  # total_cost(n) must never exceed this * n


def append_costs(n: int) -> list[int]:
    """Simulate `n` appends into a dynamic array that starts at
    capacity 1 and doubles its capacity whenever it's full. Return the
    cost of each individual append, in order.

    Cost model: a normal append (room available) costs 1. An append
    that triggers a resize costs `current_size + 1` -- current_size to
    copy every existing element into the new backing array, plus 1 for
    the append itself.

    append_costs(1) -> [1]
    append_costs(4) -> [1, 2, 3, 1]
        # append 1: size 0 -> 1, capacity 1, fits          -> cost 1
        # append 2: size 1 == capacity 1, resize to 2       -> cost 1 + 1 = 2
        # append 3: size 2 == capacity 2, resize to 4       -> cost 2 + 1 = 3
        # append 4: size 3 < capacity 4, fits                -> cost 1
    append_costs(0) -> []

    Target complexity: O(n) time, O(n) space (the returned list).
    """
    raise NotImplementedError


def total_cost(n: int) -> int:
    """Return the sum of `append_costs(n)` -- the total cost of `n`
    appends.

    total_cost(4) -> 1 + 2 + 3 + 1 == 7
    total_cost(0) -> 0

    Amortized cost per append stays O(1): total_cost(n) never exceeds
    MAX_TOTAL_COST_PER_APPEND * n, no matter how large n gets.

    Target complexity: O(n) time, O(n) space.
    """
    raise NotImplementedError
