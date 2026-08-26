from ex04_flood_fill_regions import capture_regions, flood_fill


def test_flood_fill_basic():
    image = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 1],
    ]
    result = flood_fill(image, 0, 0, 2)
    assert result == [
        [2, 2, 0],
        [2, 2, 0],
        [0, 0, 1],
    ]


def test_flood_fill_same_color_is_noop():
    image = [
        [1, 1],
        [1, 1],
    ]
    result = flood_fill(image, 0, 0, 1)
    assert result == [[1, 1], [1, 1]]


def test_flood_fill_does_not_leak_across_different_color():
    image = [
        [1, 0, 1],
    ]
    result = flood_fill(image, 0, 0, 5)
    assert result == [[5, 0, 1]]


def test_flood_fill_single_cell():
    image = [[7]]
    assert flood_fill(image, 0, 0, 3) == [[3]]


def test_flood_fill_start_cell_included():
    image = [
        [0, 0],
        [0, 0],
    ]
    result = flood_fill(image, 1, 1, 9)
    assert result == [[9, 9], [9, 9]]


def test_capture_regions_basic():
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    result = capture_regions(board)
    assert result == [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"],
    ]


def test_capture_regions_all_x_unchanged():
    board = [
        ["X", "X"],
        ["X", "X"],
    ]
    assert capture_regions(board) == [["X", "X"], ["X", "X"]]


def test_capture_regions_border_o_survives():
    board = [
        ["O", "X"],
        ["X", "X"],
    ]
    assert capture_regions(board) == [["O", "X"], ["X", "X"]]


def test_capture_regions_fully_enclosed_single_o_captured():
    board = [
        ["X", "X", "X"],
        ["X", "O", "X"],
        ["X", "X", "X"],
    ]
    assert capture_regions(board) == [
        ["X", "X", "X"],
        ["X", "X", "X"],
        ["X", "X", "X"],
    ]


def test_capture_regions_entire_board_o_all_survive_via_border():
    board = [
        ["O", "O"],
        ["O", "O"],
    ]
    # every cell touches the border on a 2x2 board -> nothing enclosed
    assert capture_regions(board) == [["O", "O"], ["O", "O"]]
