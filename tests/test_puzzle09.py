from puzzles.puzzle09 import load_data
from puzzles.puzzle09 import Encoder
from puzzles.puzzle09 import check_values
from puzzles.puzzle09 import find_contiguous_set


def test_check_values():
    filename = "./data/test_data09.txt"
    input = load_data(filename)
    enc = Encoder(input[:5], 5)
    nums_to_check = input[5:]
    result = check_values(enc, nums_to_check)
    assert result == 127


def test_find_contiguous_set():
    filename = "./data/test_data09.txt"
    input = load_data(filename)
    enc = Encoder(input[:5], 5)
    nums_to_check = input[5:]
    result = check_values(enc, nums_to_check)
    assert find_contiguous_set(input, result) == 62
