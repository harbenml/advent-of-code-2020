from puzzles.puzzle11 import solve
from puzzles.puzzle11 import check_adjacent_seats
from puzzles.puzzle11 import check_visible_seats

with open("./data/test_data11.txt") as f:
    X = f.read().split("\n")


def test_solve_part_1():
    _, count = solve(X, check_adjacent_seats, 4)
    assert count == 37


def test_solve_part_2():
    _, count = solve(X, check_visible_seats, 5)
    assert count == 26
