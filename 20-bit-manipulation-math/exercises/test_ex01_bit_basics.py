from ex01_bit_basics import (
    clear_bit,
    count_set_bits,
    get_bit,
    is_power_of_two,
    set_bit,
    toggle_bit,
)


class TickInt:
    """A duck-typed int wrapper that counts every `&` it's part of.

    Used to verify count_set_bits runs Kernighan's n & (n-1) loop --
    one AND per set bit -- instead of looping over a fixed bit width
    (which would do an AND, or nothing at all, once per bit position
    regardless of how many bits are actually set).
    """

    def __init__(self, value: int, counter: list[int]) -> None:
        self.value = value
        self._counter = counter

    def _val(self, other: object) -> int:
        return other.value if isinstance(other, TickInt) else other  # type: ignore[return-value]

    def __and__(self, other: object) -> "TickInt":
        self._counter[0] += 1
        return TickInt(self.value & self._val(other), self._counter)

    def __rand__(self, other: object) -> "TickInt":
        return self.__and__(other)

    def __sub__(self, other: object) -> "TickInt":
        return TickInt(self.value - self._val(other), self._counter)

    def __bool__(self) -> bool:
        return bool(self.value)

    def __eq__(self, other: object) -> bool:
        return self.value == self._val(other)

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __gt__(self, other: object) -> bool:
        return self.value > self._val(other)

    def __lt__(self, other: object) -> bool:
        return self.value < self._val(other)

    def __repr__(self) -> str:
        return f"TickInt({self.value})"


# -- get_bit ------------------------------------------------------------


def test_get_bit_reads_set_and_clear_positions():
    assert get_bit(0b1010, 1) == 1
    assert get_bit(0b1010, 0) == 0
    assert get_bit(0b1010, 3) == 1


def test_get_bit_beyond_highest_set_bit_is_zero():
    assert get_bit(0b101, 10) == 0


# -- set_bit --------------------------------------------------------------


def test_set_bit_turns_a_zero_into_a_one():
    assert set_bit(0b0000, 2) == 0b0100


def test_set_bit_on_already_set_bit_is_a_no_op():
    assert set_bit(0b0100, 2) == 0b0100


def test_set_bit_leaves_other_bits_untouched():
    assert set_bit(0b1001, 1) == 0b1011


# -- clear_bit ------------------------------------------------------------


def test_clear_bit_turns_a_one_into_a_zero():
    assert clear_bit(0b0100, 2) == 0b0000


def test_clear_bit_on_already_clear_bit_is_a_no_op():
    assert clear_bit(0b0000, 2) == 0b0000


def test_clear_bit_leaves_other_bits_untouched():
    assert clear_bit(0b1111, 1) == 0b1101


# -- toggle_bit -------------------------------------------------------------


def test_toggle_bit_flips_one_to_zero():
    assert toggle_bit(0b0100, 2) == 0b0000


def test_toggle_bit_flips_zero_to_one():
    assert toggle_bit(0b0000, 2) == 0b0100


def test_toggle_bit_twice_is_identity():
    n = 0b10110
    assert toggle_bit(toggle_bit(n, 3), 3) == n


# -- is_power_of_two --------------------------------------------------------


def test_is_power_of_two_true_cases():
    for n in (1, 2, 4, 8, 16, 1024, 2**20):
        assert is_power_of_two(n) is True


def test_is_power_of_two_false_cases():
    for n in (0, 3, 6, 18, 100):
        assert is_power_of_two(n) is False


def test_is_power_of_two_negative_is_false():
    assert is_power_of_two(-4) is False
    assert is_power_of_two(-1) is False


# -- count_set_bits -----------------------------------------------------


def test_count_set_bits_typical():
    assert count_set_bits(0b1011) == 3


def test_count_set_bits_zero():
    assert count_set_bits(0) == 0


def test_count_set_bits_all_ones():
    assert count_set_bits(0b1111111) == 7


def test_count_set_bits_single_high_bit_in_a_wide_number():
    assert count_set_bits(1 << 40) == 1


def test_count_set_bits_matches_brute_force_over_a_range():
    for n in range(512):
        assert count_set_bits(n) == n.bit_count()


def test_count_set_bits_uses_kernighan_trick_not_a_bit_width_loop():
    # A number with a huge bit width (60 bits) but only 3 set bits.
    # Kernighan's n & (n-1) loop performs exactly one AND per set bit;
    # a loop over bit positions (e.g. `for i in range(64)`) would do
    # dozens of ANDs (or none at all, if it uses shifts instead) --
    # either way it wouldn't cost exactly 3 ANDs.
    counter = [0]
    huge_few_bits = (1 << 59) | (1 << 30) | 1
    n = TickInt(huge_few_bits, counter)

    result = count_set_bits(n)  # type: ignore[arg-type]

    assert result == 3
    assert counter[0] == 3
