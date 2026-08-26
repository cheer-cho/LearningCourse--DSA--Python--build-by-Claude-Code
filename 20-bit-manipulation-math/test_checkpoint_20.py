from checkpoint_20 import (
    find_faulty_sensor,
    firmware_grid_rotate,
    parity_report,
    prime_channel_ids,
)

# -- parity_report ------------------------------------------------------


def test_parity_report_typical():
    report = parity_report([5, 3, 6])
    assert report == {"per_packet_bit_counts": [2, 2, 2], "overall_checksum": 0}


def test_parity_report_empty():
    report = parity_report([])
    assert report == {"per_packet_bit_counts": [], "overall_checksum": 0}


def test_parity_report_single_packet():
    report = parity_report([12])
    assert report == {"per_packet_bit_counts": [2], "overall_checksum": 12}


def test_parity_report_detects_odd_corruption_via_checksum():
    clean = parity_report([5, 3, 6])
    corrupted = parity_report([5, 3, 7])  # one bit flipped in the last packet
    assert clean["overall_checksum"] != corrupted["overall_checksum"]


# -- find_faulty_sensor ---------------------------------------------------


def test_find_faulty_sensor_typical():
    assert find_faulty_sensor([7, 3, 7, 5, 3]) == 5


def test_find_faulty_sensor_single_reading():
    assert find_faulty_sensor([42]) == 42


def test_find_faulty_sensor_faulty_reading_at_the_start():
    assert find_faulty_sensor([9, 4, 4, 6, 6]) == 9


# -- firmware_grid_rotate ---------------------------------------------------


def test_firmware_grid_rotate_typical():
    grid = [[1, 2], [3, 4]]
    firmware_grid_rotate(grid)
    assert grid == [[3, 1], [4, 2]]


def test_firmware_grid_rotate_larger_grid():
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    firmware_grid_rotate(grid)
    assert grid == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]


def test_firmware_grid_rotate_single_cell_is_unchanged():
    grid = [[1]]
    firmware_grid_rotate(grid)
    assert grid == [[1]]


# -- prime_channel_ids ------------------------------------------------------


def test_prime_channel_ids_typical():
    assert prime_channel_ids(20) == [2, 3, 5, 7, 11, 13, 17, 19]


def test_prime_channel_ids_below_two_is_empty():
    assert prime_channel_ids(1) == []
    assert prime_channel_ids(0) == []


def test_prime_channel_ids_matches_brute_force():
    def is_prime_brute(k: int) -> bool:
        if k < 2:
            return False
        return all(k % d != 0 for d in range(2, k))

    expected = [k for k in range(2, 151) if is_prime_brute(k)]
    assert prime_channel_ids(150) == expected


def test_prime_channel_ids_large_limit_is_efficient():
    ids = prime_channel_ids(1_000_000)
    assert len(ids) == 78_498
    assert ids[0] == 2
    assert ids[-1] == 999_983
