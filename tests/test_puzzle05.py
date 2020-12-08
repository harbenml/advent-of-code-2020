from puzzles.puzzle05 import parse_boarding_pass
import pytest


@pytest.mark.parametrize(
    "test_input, expected",
    [("BFFFBBFRRR", 567), ("FFFBBBFRRR", 119), ("BBFFBBFRLL", 820),],
)
def test_parse_boarding_pass(test_input, expected):
    seat_id = parse_boarding_pass(test_input)
    assert seat_id == expected
