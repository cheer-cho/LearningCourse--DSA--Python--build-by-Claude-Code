from checkpoint_15 import can_two_team, degrees_of_separation, friend_circles, suggested_friends


def test_friend_circles_basic():
    edges = [(0, 1), (1, 2), (3, 4)]
    assert friend_circles(edges, 5) == 2


def test_friend_circles_no_edges_everyone_alone():
    assert friend_circles([], 3) == 3


def test_friend_circles_all_connected():
    edges = [(0, 1), (1, 2), (2, 3)]
    assert friend_circles(edges, 4) == 1


def test_degrees_of_separation_basic():
    edges = [(0, 1), (1, 2), (2, 3)]
    assert degrees_of_separation(edges, 0, 3) == 3


def test_degrees_of_separation_disconnected():
    edges = [(0, 1), (2, 3)]
    assert degrees_of_separation(edges, 0, 3) == -1


def test_degrees_of_separation_same_user():
    edges = [(0, 1)]
    assert degrees_of_separation(edges, 0, 0) == 0


def test_degrees_of_separation_direct_friends():
    edges = [(0, 1)]
    assert degrees_of_separation(edges, 0, 1) == 1


def test_suggested_friends_basic():
    edges = [(0, 1), (1, 2), (1, 3), (2, 3)]
    assert suggested_friends(edges, 0) == [2, 3]


def test_suggested_friends_already_direct_friend_excluded():
    assert suggested_friends([(0, 1)], 0) == []


def test_suggested_friends_no_friends_at_all():
    assert suggested_friends([], 5) == []


def test_suggested_friends_sorted_no_duplicates():
    # user 0's friend is 1; 1's friends include 2 and 3 (both suggested,
    # and 2/3 also share other mutual connections that must not
    # duplicate them in the result)
    edges = [(0, 1), (1, 2), (1, 3), (2, 4), (3, 4), (2, 3)]
    result = suggested_friends(edges, 0)
    assert result == sorted(set(result))
    assert result == [2, 3]


def test_can_two_team_true():
    edges = [(0, 1), (1, 2)]
    assert can_two_team(edges, 3) is True


def test_can_two_team_triangle_false():
    edges = [(0, 1), (1, 2), (2, 0)]
    assert can_two_team(edges, 3) is False


def test_can_two_team_isolated_users_true():
    assert can_two_team([], 4) is True


def test_can_two_team_disconnected_one_bad_group_fails_whole():
    edges = [(0, 1), (2, 3), (3, 4), (4, 2)]
    assert can_two_team(edges, 5) is False


def test_large_social_graph_is_fast():
    # 50,000 edges along a single long chain 0-1-2-...-50000: O(n) BFS
    # must handle this instantly; an O(n^2) approach would not.
    n = 50_001
    edges = [(i, i + 1) for i in range(n - 1)]
    assert friend_circles(edges, n) == 1
    assert degrees_of_separation(edges, 0, n - 1) == n - 1
    assert can_two_team(edges, n) is True
