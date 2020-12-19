from typing import List
from typing import Dict
from typing import Tuple


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


def check_tickets(data: List) -> Tuple[List[int], List[int]]:
    rules = parse_rules(data[0])
    entries, _ = get_entries(data)
    invalid_nums = []
    invalid_tickets = []
    for idx, entry in enumerate(entries):
        valid_number = [False] * len(entry)
        for i, num in enumerate(entry):
            checks = check_num_against_rules(rules, num)
            valid_number[i] = any(checks)
            if not any(checks):
                invalid_nums.append(num)

        if not all(valid_number):
            invalid_tickets.append(idx)

    return invalid_nums, invalid_tickets


def check_num_against_rules(rules: Dict, num: int) -> List[bool]:
    """
    The number is checked against all rules.
    The list `checks` delivers True/False for each rule (of the current ticket field).

    e.g.
    num = 7

    rules = {
        class: [1, 3,  5, 7]
        row: [6, 11,  33, 44]
        seat: [13, 40,  45, 50]
    }

    leads to

    checks = [True, True, False]

    """
    checks = [False] * len(rules)
    for j, r in enumerate(rules.values()):
        for k in range(0, len(r) - 1, 2):

            if r[k] <= num <= r[k + 1]:
                checks[j] = True
    return checks


def get_entries(data: List) -> List:
    tickets = data[1:]
    my_ticket = tickets[0]
    my_entries = my_ticket[1].split(",")
    my_entries = [int(el) for el in my_entries]

    entries = []
    for entry in tickets[1][1:]:
        entry = entry.split(",")
        entry = [int(el) for el in entry]
        entries.append(entry)
    return entries, my_entries


def remove_unvalid_tickets(invalid_tickets: List[int], entries: List):
    return [entry for i, entry in enumerate(entries) if i not in invalid_tickets]


def find_num_positions_for_rule_fields(
    rules: Dict, entries: List, my_entries: List
) -> Dict:
    matrix = [my_entries] + entries
    num_cols = len(matrix[0])
    field_map = {key: list(range(num_cols)) for key in rules.keys()}
    """
    class 0 1 2
    row   0 1 2
    seat  0 1 2
    
    Now erase all map values, that are not valid

    """
    for col in range(num_cols):
        nums_in_col = [row[col] for row in matrix]
        for num in nums_in_col:
            checks = check_num_against_rules(rules, num)
            if not all(checks):
                field_map = update_field_map(field_map, rules, num, col, checks)
                single_entry_keys = [k for k, v in field_map.items() if len(v) == 1]
                if single_entry_keys == list(field_map):
                    # only single entries in field map
                    return field_map

    return field_map


def update_field_map(
    field_map: Dict, rules: Dict, num: int, pos: int, checks: List[bool]
) -> Dict:
    invalid_rule_idx = [i for i, x in enumerate(checks) if not x]
    rule_keys = list(field_map)
    for idx in invalid_rule_idx:
        if pos in field_map[rule_keys[idx]]:
            field_map[rule_keys[idx]].remove(pos)
            if len(field_map[rule_keys[idx]]) == 1:
                field_map = remove_pos_in_other_fields(
                    field_map, rule_keys, rule_keys[idx]
                )

    single_entry_keys = [k for k, v in field_map.items() if len(v) == 1]
    for key in single_entry_keys:
        field_map = remove_pos_in_other_fields(field_map, rule_keys, key)

    return field_map


def remove_pos_in_other_fields(field_map, rule_keys, key):
    pos_to_remove = field_map[key][0]
    for k, value in field_map.items():
        if pos_to_remove in value and k != key:
            field_map[k].remove(pos_to_remove)
    return field_map


def solve_part_1(filename: str) -> int:
    data = get_data(filename)
    invalid_nums, invalid_tickets = check_tickets(data)
    return sum(invalid_nums)


def solve_part_2(filename: str) -> int:
    data = get_data(filename)
    invalid_nums, invalid_tickets = check_tickets(data)
    rules = parse_rules(data[0])
    entries, my_entries = get_entries(data)
    entries = remove_unvalid_tickets(invalid_tickets, entries)
    field_map = find_num_positions_for_rule_fields(rules, entries, my_entries)
    result = {
        "departure location": [13],
        "departure station": [14],
        "departure platform": [15],
        "departure track": [1],
        "departure date": [4],
        "departure time": [17],
    }
    x = my_entries
    return x[13] * x[14] * x[15] * x[1] * x[4] * x[17]


if __name__ == "__main__":
    filename = "./data/data16.txt"
    data = get_data(filename)

    invalid_nums, invalid_tickets = check_tickets(data)

    rules = parse_rules(data[0])
    entries, my_entries = get_entries(data)
    entries = remove_unvalid_tickets(invalid_tickets, entries)
    field_map = find_num_positions_for_rule_fields(rules, entries, my_entries)
    print(sum(invalid_nums))
    print(field_map)

    result = {
        "departure location": [13],
        "departure station": [14],
        "departure platform": [15],
        "departure track": [1],
        "departure date": [4],
        "departure time": [17],
    }
    x = my_entries
    ans = x[13] * x[14] * x[15] * x[1] * x[4] * x[17]
