from puzzles.puzzle24 import get_data
from puzzles.puzzle24 import solve_part1
from puzzles.puzzle24 import solve_part2

fn = "./data/test_data24.txt"


def test_solve_part1():
    data = get_data(fn)
    result = solve_part1(data)
    assert len(result) == 10


def test_solve_part2():
    data = get_data(fn)
    black_tiles = solve_part1(data)
    result = solve_part2(black_tiles)
    assert result == 2208

