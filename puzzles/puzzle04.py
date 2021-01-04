import numpy as np  # type: ignore
from typing import List, Tuple, Dict
import re


def load_data(filename: str) -> List:
    with open(filename) as f:
        X = f.readlines()
    return X


def preprocess_data(X: List) -> List[Dict]:
    # remove \n at end of line
    X = [x.strip() for x in X]
    # split at whitespaces
    X = [el.split() for el in X]
    # create dictionary
    field_dict = collect_dict(X)
    return field_dict


def collect_dict(X: List) -> List[Dict]:
    fields = []
    field = {}
    for el in X:
        if el:
            field.update(dict(e.split(":") for e in el))
        else:
            fields.append(field)
            field = {}
    fields.append(field)
    return fields


def check_fields(field: List[str]) -> bool:
    valid = False
    if len(field) == 8:
        valid = sorted(field) == [
            "byr",
            "cid",
            "ecl",
            "eyr",
            "hcl",
            "hgt",
            "iyr",
            "pid",
        ]
    elif len(field) == 7:
        valid = sorted(field) == ["byr", "ecl", "eyr", "hcl", "hgt", "iyr", "pid"]
    return valid


def check_height(value: str) -> bool:
    unit = re.findall("[a-z]{2}", value)
    height = int(re.findall("[0-9]+", value)[0])
    if unit and unit[0] == "cm":
        return 150 <= height <= 193
    elif unit and unit[0] == "in":
        return 59 <= height <= 76
    return False


def check_value(field: str, value: str) -> bool:
    if field == "byr":
        return len(value) == 4 and 1920 <= int(value) <= 2002
    if field == "iyr":
        return len(value) == 4 and 2010 <= int(value) <= 2020
    if field == "eyr":
        return len(value) == 4 and 2020 <= int(value) <= 2030
    if field == "hgt":
        return check_height(value)
    if field == "hcl":
        return re.match("^#[0-9a-f]{6}", value) is not None
    if field == "ecl":
        return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if field == "pid":
        return len(value) == 9 and value.isdigit()
    if field == "cid":
        return True
    return False


def check_values(passport: dict) -> bool:
    results = [check_value(i, passport[i]) for i in passport]
    return all(results)


def get_no_valid_passports(filename: str) -> Tuple[int, int]:
    X = load_data(filename)
    passports = preprocess_data(X)
    no_valid_passports = 0
    no_valid_passports_strict = 0
    for p in passports:
        if check_fields(list(p.keys())):
            no_valid_passports += 1
            if check_values(p):
                no_valid_passports_strict += 1
    return no_valid_passports, no_valid_passports_strict


if __name__ == "__main__":

    filename = "./data/data04.txt"
    print(get_no_valid_passports(filename))
