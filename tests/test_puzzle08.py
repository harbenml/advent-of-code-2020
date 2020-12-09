from puzzles.puzzle08 import load_data
from puzzles.puzzle08 import follow_instructions
from puzzles.puzzle08 import permute_x_until_success


def test_follow_instructions():
    X = load_data("./data/test_data08.txt")
    result, state = follow_instructions(X)
    assert result == 5
    assert state == False


def test_follow_instructions_part_2():
    X = load_data("./data/test_data08_2.txt")
    result, state = follow_instructions(X)
    assert result == 8
    assert state == True


def test_permute_x_until_success():
    X = load_data("./data/test_data08.txt")
    result = permute_x_until_success(X)
    assert result == 8

