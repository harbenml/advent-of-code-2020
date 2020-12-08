from puzzles.puzzle06 import load_data
from puzzles.puzzle06 import get_sum_of_counts
from puzzles.puzzle06 import get_sum_of_counts_everyone

filename = "./data/test_data06.txt"


def test_get_sum_of_counts():
    X, X_unique, _ = load_data(filename)
    result = get_sum_of_counts(X, X_unique)
    assert result == 11


def test_get_sum_of_counts_everyone():
    X, X_unique, no_people = load_data(filename)
    result = get_sum_of_counts_everyone(X, X_unique, no_people)
    assert result == 6
