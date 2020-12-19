from puzzles.puzzle16 import solve_part_1
from puzzles.puzzle16 import solve_part_2


def test_solve_part1():
    result = solve_part_1("./data/test_data16.txt")
    assert result == 71


def test_solve_part2():
    result = solve_part_2("./data/data16.txt")
    assert result == 998358379943
