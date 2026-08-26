from checkpoint_08 import find_path, largest_file, max_tree_depth, total_size


def sample_tree() -> dict:
    return {
        "name": "root",
        "size": 0,
        "children": [
            {"name": "notes.txt", "size": 120, "children": []},
            {
                "name": "sub",
                "size": 0,
                "children": [
                    {"name": "photo.png", "size": 2048, "children": []},
                    {"name": "empty_dir", "size": 0, "children": []},
                ],
            },
        ],
    }


def build_deep_chain(depth: int) -> dict:
    """A single-branch chain `depth` nodes deep, ending in one leaf file.
    Depth 3,000 sits well above Python's default recursion limit (1000),
    proving a naive recursive walk would overflow it.
    """
    node: dict = {"name": "treasure.txt", "size": 999_999, "children": []}
    for i in range(depth - 1, 0, -1):
        node = {"name": f"dir{i}", "size": 0, "children": [node]}
    return node


def test_total_size_single_file():
    assert total_size({"name": "a", "size": 5, "children": []}) == 5


def test_total_size_sums_whole_tree():
    assert total_size(sample_tree()) == 120 + 2048


def test_max_tree_depth_single_file():
    assert max_tree_depth({"name": "a", "size": 5, "children": []}) == 1


def test_max_tree_depth_typical():
    assert max_tree_depth(sample_tree()) == 3


def test_find_path_to_nested_file():
    assert find_path(sample_tree(), "photo.png") == ["root", "sub", "photo.png"]


def test_find_path_to_root_itself():
    assert find_path(sample_tree(), "root") == ["root"]


def test_find_path_missing_name_returns_none():
    assert find_path(sample_tree(), "nope.txt") is None


def test_largest_file_ignores_directories():
    assert largest_file(sample_tree()) == "photo.png"


def test_largest_file_breaks_ties_by_traversal_order():
    tree = {
        "name": "root",
        "size": 0,
        "children": [
            {"name": "a.txt", "size": 10, "children": []},
            {"name": "b.txt", "size": 10, "children": []},
        ],
    }
    assert largest_file(tree) == "a.txt"


def test_largest_file_when_root_itself_is_the_only_leaf():
    tree = {"name": "solo.txt", "size": 0, "children": []}
    assert largest_file(tree) == "solo.txt"


def test_deep_chain_survives_recursion_limit_depth():
    depth = 3_000
    tree = build_deep_chain(depth)

    assert total_size(tree) == 999_999
    assert max_tree_depth(tree) == depth
    assert find_path(tree, "treasure.txt") is not None
    assert len(find_path(tree, "treasure.txt")) == depth
    assert largest_file(tree) == "treasure.txt"
