# Scenario: a delivery van drives a circular route between fuel depots,
# gaining `gas[i]` fuel and spending `cost[i]` fuel between depot `i`
# and depot `i+1`. Pattern: greedy net-balance sweep.
# Run: uv run pytest 17-greedy-intervals -k ex03


def start_station(gas: list[int], cost: list[int]) -> int:
    """`gas` and `cost` are same-length lists describing `n` depots
    arranged in a circle: starting at depot `i` with an empty tank,
    you gain `gas[i]` fuel then spend `cost[i]` fuel driving to depot
    `i + 1` (wrapping around). Return the index of a depot you can
    start at to complete the full circuit without the tank ever going
    negative, or -1 if no such depot exists. Assume at most one valid
    start exists when a solution exists.

    Two insights, both needed:
    1. If `sum(gas) < sum(cost)`, no start can ever work — the total
       deficit is unavoidable no matter where the circuit begins.
    2. If `sum(gas) >= sum(cost)`, a valid start is GUARANTEED to
       exist, and it is the depot right after the running tank last
       dropped below zero — every depot before that point can only
       ever be reached with an even larger existing deficit already
       in the tank, so none of them could be a working start either.
       One sweep finds both the feasibility check and the start index.

    start_station([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) -> 3
    start_station([2, 3, 4], [3, 4, 3]) -> -1

    Target: O(n) time, O(1) space.
    """
    raise NotImplementedError
