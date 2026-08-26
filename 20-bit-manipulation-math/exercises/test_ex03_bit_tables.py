from ex03_bit_tables import count_bits_upto, reverse_bits32

# -- count_bits_upto --------------------------------------------------------


def test_count_bits_upto_typical():
    assert count_bits_upto(5) == [0, 1, 1, 2, 1, 2]


def test_count_bits_upto_zero():
    assert count_bits_upto(0) == [0]


def test_count_bits_upto_length_matches_n_plus_one():
    result = count_bits_upto(10)
    assert len(result) == 11


def test_count_bits_upto_matches_brute_force():
    n = 1000
    result = count_bits_upto(n)
    expected = [i.bit_count() for i in range(n + 1)]
    assert result == expected


def test_count_bits_upto_large_n_is_efficient():
    n = 300_000
    result = count_bits_upto(n)
    assert len(result) == n + 1
    # Spot-check rather than compare the whole list (keeps the test fast).
    assert result[0] == 0
    assert result[1] == 1
    assert result[7] == 3          # 0b111
    assert result[255] == 8        # 0b11111111
    assert result[256] == 1        # 0b100000000
    assert result[n] == n.bit_count()


# -- reverse_bits32 --------------------------------------------------------


def test_reverse_bits32_small_value():
    assert reverse_bits32(0b1011) == 0b11010000000000000000000000000000


def test_reverse_bits32_zero():
    assert reverse_bits32(0) == 0


def test_reverse_bits32_all_ones():
    assert reverse_bits32(0xFFFFFFFF) == 0xFFFFFFFF


def test_reverse_bits32_single_low_bit_moves_to_top():
    assert reverse_bits32(1) == 1 << 31


def test_reverse_bits32_single_high_bit_moves_to_bottom():
    assert reverse_bits32(1 << 31) == 1


def test_reverse_bits32_is_its_own_inverse():
    for n in (0, 1, 0b1010101010, 0xABCD1234, 0xFFFFFFFF):
        assert reverse_bits32(reverse_bits32(n)) == n
