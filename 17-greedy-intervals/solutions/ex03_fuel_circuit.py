def start_station(gas: list[int], cost: list[int]) -> int:
    # Pattern: greedy net-balance sweep. If the total surplus is
    # negative, no start works. Otherwise the answer is the index
    # right after the running tank last went negative — everything
    # before that point carries an even bigger deficit into any
    # attempt, so it can never be a valid start either.
    # Complexity: O(n) time, O(1) space.
    if len(gas) == 0:
        return -1

    total_surplus = 0
    running_tank = 0
    candidate_start = 0

    for i in range(len(gas)):
        delta = gas[i] - cost[i]
        total_surplus += delta
        running_tank += delta
        if running_tank < 0:
            candidate_start = i + 1
            running_tank = 0

    return candidate_start if total_surplus >= 0 else -1
