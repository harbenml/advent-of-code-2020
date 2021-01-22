from puzzles.puzzle03 import load_data
from puzzles.puzzle03 import count_trees

filename = "./data/test_data03.txt"
X = load_data(filename)


def test_count_trees():
    moves = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    multi = 1
    for move in moves:
        multi *= count_trees(X, *move)

    assert multi == 336
