from puzzles.puzzle08 import load_data
from puzzles.puzzle08 import follow_instructions
from puzzles.puzzle08 import permute_x_until_success

X = load_data("./data/test_data08.txt")
Y = load_data("./data/test_data08_2.txt")


def test_follow_instructions():
    result, state = follow_instructions(X)
    assert result == 5
    assert state == False


def test_follow_instructions_part_2():
    result2, state2 = follow_instructions(Y)
    assert result2 == 8
    assert state2 == True


def test_permute_x_until_success():
    result3 = permute_x_until_success(X)
    assert result3 == 8

