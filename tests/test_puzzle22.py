from puzzles.puzzle22 import solve_part1
from puzzles.puzzle22 import solve_part2

fn = "./data/test_data22.txt"


def test_solve_part1():
    result = solve_part1(fn)
    assert result == 306


def test_solve_part2():
    result = solve_part2(fn)
    assert result == 291
