from ex07_k_stops_cheapest import cheapest_within_k_stops


def test_one_stop_allows_the_cheaper_layover_route():
    flights = [(0, 1, 100), (1, 2, 100), (0, 2, 500)]
    assert cheapest_within_k_stops(3, flights, 0, 2, 1) == 200


def test_zero_stops_forces_the_direct_flight():
    flights = [(0, 1, 100), (1, 2, 100), (0, 2, 500)]
    assert cheapest_within_k_stops(3, flights, 0, 2, 0) == 500


def test_no_route_returns_none():
    assert cheapest_within_k_stops(2, [], 0, 1, 5) is None


def test_source_equals_destination_costs_zero():
    flights = [(0, 1, 100)]
    assert cheapest_within_k_stops(2, flights, 0, 0, 3) == 0


def test_not_enough_stops_makes_route_unreachable():
    # Only route is 0->1->2->3 (2 stops); allowing just 1 stop can't
    # reach node 3 at all.
    flights = [(0, 1, 1), (1, 2, 1), (2, 3, 1)]
    assert cheapest_within_k_stops(4, flights, 0, 3, 1) is None
    assert cheapest_within_k_stops(4, flights, 0, 3, 2) == 3


def test_extra_stop_budget_does_not_change_the_cheapest_price():
    flights = [(0, 1, 100), (1, 2, 100), (0, 2, 500)]
    assert cheapest_within_k_stops(3, flights, 0, 2, 10) == 200


def test_ignores_a_more_expensive_route_with_fewer_stops():
    # Direct flight is pricier than the two-hop route, and the stop
    # budget comfortably allows the two-hop route.
    flights = [(0, 1, 1), (1, 2, 1), (0, 2, 1000)]
    assert cheapest_within_k_stops(3, flights, 0, 2, 5) == 2
