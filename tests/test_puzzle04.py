from puzzles.puzzle04 import get_no_valid_passports
import pytest


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("./data/test_data04.txt", (2, 2)),
        ("./data/test_data04_2.txt", (4, 4)),
        ("./data/test_data04_3.txt", (4, 0)),
    ],
)
def test_get_no_valid_passports(test_input, expected):
    no_valid = get_no_valid_passports(test_input)
    assert no_valid == expected
