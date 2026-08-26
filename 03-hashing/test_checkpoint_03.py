from checkpoint_03 import action_counts, first_unique_user, has_duplicate_burst, users_by_action


def test_action_counts_typical():
    events = [("ada", "login"), ("bo", "login"), ("ada", "logout")]
    assert action_counts(events) == {"login": 2, "logout": 1}


def test_action_counts_empty_events():
    assert action_counts([]) == {}


def test_action_counts_single_event():
    assert action_counts([("ada", "login")]) == {"login": 1}


def test_first_unique_user_typical():
    events = [("ada", "login"), ("bo", "login"), ("ada", "logout"), ("cy", "login")]
    assert first_unique_user(events) == "bo"


def test_first_unique_user_none_when_all_repeat():
    events = [("ada", "login"), ("bo", "login"), ("ada", "logout"), ("bo", "logout")]
    assert first_unique_user(events) is None


def test_first_unique_user_empty_events():
    assert first_unique_user([]) is None


def test_first_unique_user_single_event():
    assert first_unique_user([("ada", "login")]) == "ada"


def test_users_by_action_typical():
    events = [("ada", "login"), ("bo", "login"), ("ada", "logout")]
    assert users_by_action(events) == {"login": ["ada", "bo"], "logout": ["ada"]}


def test_users_by_action_repeated_user_repeated_action():
    events = [("ada", "login"), ("ada", "login")]
    assert users_by_action(events) == {"login": ["ada", "ada"]}


def test_users_by_action_empty_events():
    assert users_by_action([]) == {}


def test_has_duplicate_burst_within_k():
    events = [("ada", "login"), ("bo", "login"), ("ada", "login")]
    assert has_duplicate_burst(events, 2) is True


def test_has_duplicate_burst_too_far_apart():
    events = [("ada", "login"), ("bo", "login"), ("ada", "login")]
    assert has_duplicate_burst(events, 1) is False


def test_has_duplicate_burst_different_action_not_a_burst():
    events = [("ada", "login"), ("ada", "logout")]
    assert has_duplicate_burst(events, 5) is False


def test_has_duplicate_burst_empty_events():
    assert has_duplicate_burst([], 3) is False


def test_checkpoint_efficiency_large_input():
    # 100_000 events across a small pool of users/actions so every
    # function has real repetition to chase. An O(n^2) "compare every
    # event to every other event" approach would be far too slow here;
    # these hash-map patterns handle it instantly.
    n = 100_000
    users = [f"user{i}" for i in range(50)]
    actions = ["login", "logout", "click", "purchase"]
    events = [(users[i % len(users)], actions[i % len(actions)]) for i in range(n)]

    counts = action_counts(events)
    assert sum(counts.values()) == n
    assert set(counts.keys()) == set(actions)

    grouped = users_by_action(events)
    assert sum(len(v) for v in grouped.values()) == n

    # every user repeats many times at this size, so no unique user exists
    assert first_unique_user(events) is None

    # Every (user, action) pair recurs every lcm(50, 4) = 100 events, and
    # never sooner (the (user, action) sequence has minimal period 100).
    assert has_duplicate_burst(events, 99) is False
    assert has_duplicate_burst(events, 100) is True
