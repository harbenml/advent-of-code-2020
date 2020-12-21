from typing import Any
from typing import Dict
from typing import List
from typing import Tuple

from collections import deque


def get_rules(fn: str) -> Tuple[Dict[int, List], List[str]]:
    rules_raw, codes_raw = open(fn).read().split("\n\n")
    rules: Dict[int, Any] = {}

    for r in rules_raw.split("\n"):
        rules[int(r.split(": ")[0])] = r.split(": ")[1]

    for k, v in rules.items():
        if len(v) == 3 and not v[0] == '"':
            rules[k] = [int(el) for el in v.split(" ")]
        elif len(v) > 3:
            ans = [el for el in v.split(" | ")]
            r = []
            for a in ans:
                r.append([int(el) for el in a.split(" ")])
            rules[k] = r
        else:
            rules[k] = v.strip('"')
            if v.isnumeric():
                rules[k] = [[int(v)]]

    codes = codes_raw.split("\n")
    return rules, codes


def check_code(code: str, rules: Dict[int, List]) -> bool:

    queue = deque([(code, [0])])

    while queue:

        code, rules_to_check = queue.popleft()

        if not code and not rules_to_check:
            return True
        elif not code or not rules_to_check:
            continue

        current_rules = rules[rules_to_check[0]]
        rules_to_check = rules_to_check[1:]

        if current_rules == code[0]:
            queue.append((code[1:], rules_to_check))
        elif isinstance(current_rules, list):
            for rule in current_rules:
                if isinstance(rule, int):
                    rule = [rule]
                queue.append((code, rule + rules_to_check))
    return False


if __name__ == "__main__":

    filename = "./data/test_data19_2.txt"
    rules, codes = get_rules(filename)

    num_valid_codes = 0
    for code in codes:
        num_valid_codes += check_code(code, rules)

    print("solution part 1:", num_valid_codes)

    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]

    num_valid_codes = 0
    for code in codes:
        num_valid_codes += check_code(code, rules)

    print("solution part 2:", num_valid_codes)

