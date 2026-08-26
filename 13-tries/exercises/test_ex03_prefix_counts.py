from ex03_prefix_counts import PrefixCounter


def test_count_starting_with_shared_prefix():
    pc = PrefixCounter()
    pc.insert("car")
    pc.insert("card")
    pc.insert("cat")
    assert pc.count_starting_with("ca") == 3
    assert pc.count_starting_with("car") == 2
    assert pc.count_starting_with("cat") == 1


def test_count_starting_with_unknown_prefix_is_zero():
    pc = PrefixCounter()
    pc.insert("car")
    assert pc.count_starting_with("z") == 0


def test_count_starting_with_empty_prefix_is_total_words():
    pc = PrefixCounter()
    for word in ["car", "card", "cat", "dog"]:
        pc.insert(word)
    assert pc.count_starting_with("") == 4


def test_count_starting_with_duplicate_insert_counts_once_per_insert_call():
    pc = PrefixCounter()
    pc.insert("car")
    pc.insert("car")
    assert pc.count_starting_with("car") == 2


def test_autocomplete_alphabetical_order():
    pc = PrefixCounter()
    for word in ["care", "card", "car"]:
        pc.insert(word)
    assert pc.autocomplete("car", 10) == ["car", "card", "care"]


def test_autocomplete_respects_k():
    pc = PrefixCounter()
    for word in ["care", "card", "car"]:
        pc.insert(word)
    assert pc.autocomplete("car", 2) == ["car", "card"]


def test_autocomplete_no_matches_returns_empty():
    pc = PrefixCounter()
    pc.insert("car")
    assert pc.autocomplete("dog", 5) == []


def test_autocomplete_prefix_itself_is_a_word():
    pc = PrefixCounter()
    pc.insert("car")
    pc.insert("card")
    assert pc.autocomplete("car", 1) == ["car"]


def test_autocomplete_k_zero_returns_empty():
    pc = PrefixCounter()
    pc.insert("car")
    assert pc.autocomplete("car", 0) == []


def test_efficiency_ten_thousand_words_many_queries():
    # 50 groups of 200 words each -> 10_000 words total, with predictable
    # counts per group prefix. A naive "scan every word" implementation
    # of count_starting_with would be O(n * P) per call; a real trie
    # answers straight from the node's counter in O(P), so thousands of
    # queries against 10_000 words stay effectively instant.
    pc = PrefixCounter()
    groups = 50
    per_group = 200
    for g in range(groups):
        for j in range(per_group):
            pc.insert(f"g{g:02d}i{j:03d}")

    assert pc.count_starting_with("") == groups * per_group

    for g in range(groups):
        prefix = f"g{g:02d}"
        assert pc.count_starting_with(prefix) == per_group

    # Many repeated queries against the same large trie.
    for _ in range(2_000):
        assert pc.count_starting_with("g00") == per_group

    assert pc.count_starting_with("g99") == 0

    suggestions = pc.autocomplete("g00i00", 3)
    assert suggestions == ["g00i000", "g00i001", "g00i002"]
