from puzzles.puzzle12 import Ferry1
from puzzles.puzzle12 import Ferry2


def test_part_1():
    boat = Ferry1()
    actions = ["F10", "N3", "F7", "R90", "F11"]
    boat.process_actions(actions)
    assert boat.get_distance() == 25


def test_part_2():
    boat = Ferry2()
    actions = ["F10", "N3", "F7", "R90", "F11"]
    boat.process_actions(actions)
    assert boat.get_distance() == 286
