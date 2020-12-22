from puzzles.puzzle20 import get_data
from puzzles.puzzle20 import solve_part1


def test_solve_part1():
    fn = "./data/test_data20.txt"
    tiles = get_data(fn)
    result = solve_part1(tiles)
    assert result == 20899048083289
