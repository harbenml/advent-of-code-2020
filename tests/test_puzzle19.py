from puzzles.puzzle19 import check_code
from puzzles.puzzle19 import get_rules


def test_part1():
    filename = "./data/test_data19.txt"
    rules, codes = get_rules(filename)
    num_valid_codes = 0
    for code in codes:
        num_valid_codes += check_code(code, rules)

    print("solution part 1:", num_valid_codes)
    assert num_valid_codes == 2


def test_part2():
    filename = "./data/test_data19_2.txt"
    rules, codes = get_rules(filename)
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]

    num_valid_codes = 0
    for code in codes:
        num_valid_codes += check_code(code, rules)

    assert num_valid_codes == 12
