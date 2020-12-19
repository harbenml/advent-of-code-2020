from puzzles.puzzle17 import get_data
from puzzles.puzzle17 import simulate_one_cycle


filename = "./data/test_data17.txt"


def test_solve_part1():
    active = get_data(filename, 3)
    for _ in range(6):
        active = simulate_one_cycle(active, 3)
    assert len(active) == 112


def test_solve_part2():
    active = get_data(filename, 4)
    for _ in range(6):
        active = simulate_one_cycle(active, 4)
    assert len(active) == 848
