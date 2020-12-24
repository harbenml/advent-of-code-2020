from puzzles.puzzle20 import get_data
from puzzles.puzzle20 import solve_part1
from puzzles.puzzle20 import solve_part2

fn = "./data/test_data20.txt"


def test_solve_part1():
    result = solve_part1(fn)
    assert result == 20899048083289


def test_solve_part2():
    result = solve_part2(fn)
    assert result == 273
