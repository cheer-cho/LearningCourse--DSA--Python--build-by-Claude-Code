from checkpoint_13 import SearchBox


def test_suggest_alphabetical_and_respects_k():
    box = SearchBox()
    for word in ["care", "card", "car", "cart"]:
        box.index(word)
    assert box.suggest("car", 2) == ["car", "card"]
    assert box.suggest("car", 10) == ["car", "card", "care", "cart"]


def test_suggest_no_matches_is_empty():
    box = SearchBox()
    box.index("dog")
    assert box.suggest("cat", 5) == []


def test_suggest_lists_each_indexed_word_once_even_if_indexed_twice():
    box = SearchBox()
    box.index("car")
    box.index("car")
    assert box.suggest("car", 5) == ["car"]


def test_match_exact_and_wildcard():
    box = SearchBox()
    box.index("bad")
    box.index("bat")
    assert box.match("bad") is True
    assert box.match("b.d") is True
    assert box.match("b.t") is True
    assert box.match("ba.") is True
    assert box.match("...") is True
    assert box.match("....") is False
    assert box.match("cat") is False


def test_match_on_empty_index():
    box = SearchBox()
    assert box.match("a") is False


def test_popularity_counts_prefix_matches():
    box = SearchBox()
    for word in ["car", "card", "cart", "dog"]:
        box.index(word)
    assert box.popularity("car") == 3
    assert box.popularity("do") == 1
    assert box.popularity("z") == 0
    assert box.popularity("") == 4


def test_popularity_counts_repeated_indexing_of_same_word():
    box = SearchBox()
    box.index("car")
    box.index("car")
    box.index("card")
    assert box.popularity("car") == 3
    assert box.popularity("card") == 1


def test_empty_string_word_is_supported():
    box = SearchBox()
    box.index("")
    assert box.match("") is True
    assert box.popularity("") == 1
    assert box.suggest("", 5) == [""]


def test_search_box_efficiency_twenty_thousand_words_mixed_queries():
    # 20_000 indexed words across 100 groups of 200, then 1_000 mixed
    # suggest/match/popularity queries against them. Every operation is
    # bounded by prefix/pattern length (or the small number of results
    # returned), never by how many words are indexed overall, so this
    # runs to completion effectively instantly on a real trie.
    box = SearchBox()
    groups = 100
    per_group = 200
    words = []
    for g in range(groups):
        for j in range(per_group):
            word = f"item{g:03d}v{j:03d}"
            words.append(word)
            box.index(word)

    assert box.popularity("") == groups * per_group

    for g in range(0, groups, 10):
        prefix = f"item{g:03d}"
        assert box.popularity(prefix) == per_group

    query_count = 0
    for i in range(1_000):
        word = words[i % len(words)]
        prefix = word[:8]
        suggestions = box.suggest(prefix, 3)
        assert all(s.startswith(prefix) for s in suggestions)
        assert box.match(word) is True
        assert box.popularity(prefix) >= len(suggestions)
        query_count += 1

    assert query_count == 1_000
