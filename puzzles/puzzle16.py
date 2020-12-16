from typing import List
from typing import Dict


def get_data(filename: str) -> List:
    with open(filename) as f:
        data = f.read().split("\n\n")
    data = [el.split("\n") for el in data]
    return data


def parse_rules(rules: List) -> Dict[str, List[int]]:
    y: Dict[str, List[int]] = {}
    for x in rules:
        x = x.split(": ")
        x[1] = x[1].split(" or ")
        x[1] = [el.split("-") for el in x[1]]
        x[1] = x[1][0] + x[1][1]
        x[1] = [int(el) for el in x[1]]
        y[x[0]] = x[1]
    return y


def check_tickets(entries: List, rules: Dict[str, List[int]]) -> List[int]:
    invalid_nums = []
    for t in entries:
        valid_number = [False] * len(t)
        for i, num in enumerate(t):
            check = [False] * len(rules.values())
            for j, r in enumerate(rules.values()):
                for k in range(0, len(r) - 1, 2):
                    if r[k] <= num <= r[k + 1]:
                        check[j] = True

            valid_number[i] = any(check)

            if not any(check):
                invalid_nums.append(num)

    return invalid_nums


if __name__ == "__main__":
    filename = "./data/data16.txt"
    data = get_data(filename)
    # print(data)
    rules = parse_rules(data[0])
    print(rules)

    tickets = data[1:]
    my_ticket = tickets[0]
    my_entries = my_ticket[1].split(",")
    my_entries = [int(el) for el in my_entries]
    print(my_entries)

    entries = []
    for entry in tickets[1][1:]:
        entry = entry.split(",")
        entry = [int(el) for el in entry]
        entries.append(entry)

    invalid_nums = check_tickets(entries, rules)
    print(sum(invalid_nums))
