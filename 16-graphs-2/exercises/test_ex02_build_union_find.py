from ex02_build_union_find import UnionFind


def test_starts_with_n_singleton_components():
    uf = UnionFind(5)
    assert uf.component_count() == 5
    for i in range(5):
        assert uf.find(i) == i


def test_union_merges_two_components():
    uf = UnionFind(3)
    assert uf.union(0, 1) is True
    assert uf.component_count() == 2
    assert uf.connected(0, 1) is True


def test_union_already_connected_returns_false():
    uf = UnionFind(3)
    uf.union(0, 1)
    assert uf.union(0, 1) is False
    assert uf.component_count() == 2


def test_union_is_transitive():
    uf = UnionFind(4)
    uf.union(0, 1)
    uf.union(1, 2)
    assert uf.connected(0, 2) is True
    assert uf.connected(0, 3) is False


def test_connected_false_for_unrelated_elements():
    uf = UnionFind(4)
    assert uf.connected(0, 3) is False


def test_component_count_decreases_to_one_when_fully_merged():
    uf = UnionFind(5)
    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(2, 3)
    uf.union(3, 4)
    assert uf.component_count() == 1


def test_find_after_many_unions_stays_consistent():
    uf = UnionFind(6)
    uf.union(0, 1)
    uf.union(2, 3)
    uf.union(4, 5)
    uf.union(1, 3)
    assert uf.connected(0, 2) is True
    assert uf.connected(0, 5) is False


def test_single_element_is_its_own_component():
    uf = UnionFind(1)
    assert uf.component_count() == 1
    assert uf.connected(0, 0) is True


def test_large_scale_mixed_operations_is_fast():
    # ~200_000 union/find/connected calls over 100_000 elements. Without
    # path compression AND union by rank, chains can degrade toward
    # O(n) per find -- this must complete quickly regardless.
    n = 100_000
    uf = UnionFind(n)
    for i in range(0, n - 1, 2):
        uf.union(i, i + 1)  # 50_000 unions: pairs {0,1}, {2,3}, ...
    for i in range(0, n - 3, 4):
        uf.union(i, i + 2)  # 25_000 unions: merge pairs into groups of 4

    checks = 0
    for i in range(0, n - 3, 4):
        assert uf.connected(i, i + 1) is True
        assert uf.connected(i, i + 2) is True
        assert uf.connected(i, i + 3) is True
        if i + 4 < n:
            assert uf.connected(i, i + 4) is False  # next group is disjoint
        checks += 4
    assert checks >= 100_000

    assert uf.component_count() == n // 4 + (1 if n % 4 else 0)
