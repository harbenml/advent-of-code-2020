from puzzles.puzzle13 import get_data
from puzzles.puzzle13 import solve_part_1
from puzzles.puzzle13 import solve_part_2


def test_solve_part_1():
    departure, bus_ids, _ = get_data("./data/test_data13.txt")
    assert solve_part_1(bus_ids, departure) == 295


def test_part_2():
    departure, bus_ids, delays = get_data("./data/test_data13.txt")
    assert solve_part_2(bus_ids, departure, delays) == 1068781
