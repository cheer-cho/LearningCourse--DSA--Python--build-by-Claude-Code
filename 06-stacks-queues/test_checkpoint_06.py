from checkpoint_06 import EditorHistory, spans

# ---- EditorHistory -------------------------------------------------------


def test_starts_empty():
    e = EditorHistory()
    assert e.text == ""


def test_type_appends():
    e = EditorHistory()
    e.type("cat")
    e.type(" dog")
    assert e.text == "cat dog"


def test_delete_last_removes_one_character():
    e = EditorHistory()
    e.type("cats")
    e.delete_last()
    assert e.text == "cat"


def test_delete_last_on_empty_is_a_no_op():
    e = EditorHistory()
    e.delete_last()
    assert e.text == ""


def test_undo_reverts_last_type():
    e = EditorHistory()
    e.type("cat")
    e.type("dog")
    e.undo()
    assert e.text == "cat"


def test_undo_reverts_last_delete():
    e = EditorHistory()
    e.type("cats")
    e.delete_last()
    assert e.text == "cat"
    e.undo()
    assert e.text == "cats"


def test_undo_with_no_history_is_a_no_op():
    e = EditorHistory()
    e.undo()
    assert e.text == ""


def test_redo_reapplies_undone_change():
    e = EditorHistory()
    e.type("cat")
    e.undo()
    assert e.text == ""
    e.redo()
    assert e.text == "cat"


def test_redo_with_no_undone_history_is_a_no_op():
    e = EditorHistory()
    e.type("cat")
    e.redo()
    assert e.text == "cat"


def test_typing_after_undo_clears_redo_stack():
    e = EditorHistory()
    e.type("cat")
    e.undo()
    e.type("dog")
    assert e.text == "dog"
    e.redo()  # nothing to redo — "cat" is gone forever
    assert e.text == "dog"


def test_deep_undo_redo_round_trip():
    e = EditorHistory()
    e.type("a")
    e.type("b")
    e.type("c")
    e.delete_last()  # "ab"
    e.undo()  # back to "abc"
    e.undo()  # back to "ab"
    e.undo()  # back to "a"
    assert e.text == "a"
    e.redo()
    e.redo()
    e.redo()
    assert e.text == "ab"


def test_heavily_interleaved_undo_redo():
    e = EditorHistory()
    for ch in "abcde":
        e.type(ch)
    assert e.text == "abcde"
    e.undo()
    e.undo()
    assert e.text == "abc"
    e.redo()
    assert e.text == "abcd"
    e.delete_last()
    e.delete_last()
    assert e.text == "ab"
    e.undo()
    assert e.text == "abc"
    e.undo()
    assert e.text == "abcd"
    e.undo()
    assert e.text == "abc"


# ---- spans -----------------------------------------------------------


def test_spans_classic_example():
    prices = [100, 80, 60, 70, 60, 75, 85]
    assert spans(prices) == [1, 1, 1, 2, 1, 4, 6]


def test_spans_all_equal():
    assert spans([10, 10, 10]) == [1, 2, 3]


def test_spans_strictly_decreasing():
    assert spans([5, 4, 3, 2, 1]) == [1, 1, 1, 1, 1]


def test_spans_strictly_increasing():
    assert spans([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_spans_empty():
    assert spans([]) == []


def test_spans_single_price():
    assert spans([42]) == [1]


def test_spans_large_increasing_input_is_fast():
    # Efficiency test: worst case for a naive per-day backward scan —
    # strictly increasing prices mean every day's span reaches all the
    # way back to day 0, an O(n) scan per day (O(n^2) total). A
    # monotonic stack still finishes in O(n).
    n = 100_000
    prices = list(range(1, n + 1))
    assert spans(prices) == list(range(1, n + 1))
