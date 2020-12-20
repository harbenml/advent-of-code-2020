""" Operation Order

As I found out by looking at other solutions:
The clever trick in this puzzle is to define a Number class and to use the
__sub__ method for multiplying in order to fulfill the changed operator precedence.

"""


def get_data(filename: str) -> list:
    return open("./data/data18.txt").read().split("\n")


class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, x):
        return Number(self.value + x.value)

    def __sub__(self, x):
        return Number(self.value * x.value)


def parse(input_: str) -> str:
    str_to_evaluate = ""
    for x in input_:
        if x in "0123456789":
            str_to_evaluate += "Number(" + x + ")"
        else:
            str_to_evaluate += x
    str_to_evaluate = str_to_evaluate.replace("*", "-")
    return str_to_evaluate


def solve_part1(filename: str) -> int:
    data = get_data(filename)
    result = 0
    for exp in data:
        str_to_evaluate = parse(exp)
        result += eval(str_to_evaluate).value
    return result


if __name__ == "__main__":

    input_ = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
    str_to_evaluate = parse(input_)
    print(eval(str_to_evaluate).value)

    filename = "./data/data18.txt"
    print(solve_part1(filename))
