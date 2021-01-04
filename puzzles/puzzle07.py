import re


def load_data(filename: str) -> list:
    with open(filename) as f:
        X = f.read().split("\n")
    return X


def parse_input(X: list) -> dict:
    d: dict = {}
    for x in X:
        outer = x.split(" contain ")[0].split(" ")
        outer = outer[0] + " " + outer[1]
        inner = x.split(" contain ")[1].split(", ")
        d[outer] = {}
        for i in inner:
            j = i.split(" ")
            if j != ["no", "other", "bags."]:
                d[outer].update({j[1] + " " + j[2]: int(j[0])})
    return d


def check_gold_bag(bags: dict, d: dict) -> int:
    count = 0
    colors = list(bags.keys())
    for color in colors:
        if color == "shiny gold":
            count += 1
        elif check_gold_bag(d[color], d):
            count += 1
    return count


def count_gold_bags(d: dict) -> int:
    num_gold_bags = 0
    for i in d:
        if check_gold_bag(d[i], d) > 0:
            num_gold_bags += 1
    return num_gold_bags


def count_bags_inside(d: dict, bag) -> int:
    count = 0
    if d[bag]:
        for j in d[bag]:
            count += d[bag][j] + d[bag][j] * count_bags_inside(d, j)
    return count


if __name__ == "__main__":

    filename = "./data/data07.txt"

    X = load_data(filename)
    d = parse_input(X)

    print(count_gold_bags(d))
    print(count_bags_inside(d, "shiny gold"))
