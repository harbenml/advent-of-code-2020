from puzzles.puzzle10 import load_data
from puzzles.puzzle10 import solve_part_1
from puzzles.puzzle10 import solve_part_2

filename = "./data/test_data10.txt"
X = load_data(filename)


def test_solve_part_1():
    assert solve_part_1(X) == 220


def test_solve_part_2():
    assert solve_part_2(X) == 4410
