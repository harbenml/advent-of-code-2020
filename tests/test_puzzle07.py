from puzzles.puzzle07 import count_gold_bags
from puzzles.puzzle07 import count_bags_inside
from puzzles.puzzle07 import load_data
from puzzles.puzzle07 import parse_input


def test_count_gold_bags():
    X = load_data("./data/test_data07.txt")
    my_dict = parse_input(X)
    result = count_gold_bags(my_dict)
    assert result == 4


def test_count_bags_inside():
    X = load_data("./data/test_data07_2.txt")
    my_dict = parse_input(X)
    result = count_bags_inside(my_dict, "shiny gold")
    assert result == 126
