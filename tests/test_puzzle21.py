from puzzles.puzzle21 import solve_part1
from puzzles.puzzle21 import solve_part2


def test_solve():
    fn = "./data/test_data21.txt"
    ans1, identified = solve_part1(fn)
    ans2 = solve_part2(identified)
    assert ans1 == 5
    assert ans2 == "mxmxvkd,sqjhc,fvjkl"
