from puzzles.puzzle02 import load_data
from puzzles.puzzle02 import solve_part_1
from puzzles.puzzle02 import solve_part_2

lines = load_data()


def test_solve_part_1():
    assert solve_part_1(lines) == 600


def test_solve_part_2():
    assert solve_part_2(lines) == 245
