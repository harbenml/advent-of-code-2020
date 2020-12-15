from puzzles.puzzle15 import solve

import pytest


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ([0, 3, 6], 436),
        ([1, 3, 2], 1),
        ([2, 1, 3], 10),
        ([1, 2, 3], 27),
        ([2, 3, 1], 78),
        ([3, 2, 1], 438),
        ([3, 1, 2], 1836),
    ],
)
def test_solve(test_input, expected):
    assert solve(test_input, 2020) == expected

