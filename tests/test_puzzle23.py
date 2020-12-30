from puzzles.puzzle23 import solve_part1
from puzzles.puzzle23 import solve_part2

fn = "./data/test_data23.txt"


def test_solve_part1():
    result = solve_part1(fn)
    assert result == 67384529


def test_solve_part2():
    result = solve_part2(fn)
    assert result == 149245887792

