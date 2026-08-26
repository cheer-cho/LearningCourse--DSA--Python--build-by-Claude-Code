from ex03_fuel_circuit import start_station


def test_start_station_typical():
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    assert start_station(gas, cost) == 3


def test_start_station_no_solution():
    gas = [2, 3, 4]
    cost = [3, 4, 3]
    assert start_station(gas, cost) == -1


def test_start_station_single_depot_feasible():
    assert start_station([5], [3]) == 0


def test_start_station_single_depot_infeasible():
    assert start_station([1], [3]) == -1


def test_start_station_start_at_zero():
    gas = [5, 1, 1]
    cost = [1, 1, 1]
    result = start_station(gas, cost)
    assert result == 0


def test_start_station_solution_actually_completes_circuit():
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    start = start_station(gas, cost)
    assert start != -1
    n = len(gas)
    tank = 0
    for offset in range(n):
        i = (start + offset) % n
        tank += gas[i] - cost[i]
        assert tank >= 0


def test_start_station_efficiency_large_input():
    n = 100_000
    gas = [1] * n
    cost = [1] * n
    assert start_station(gas, cost) == 0


def test_start_station_empty_input():
    assert start_station([], []) == -1
