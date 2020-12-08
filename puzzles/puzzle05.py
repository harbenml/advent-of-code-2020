from typing import Tuple, List
import numpy as np


def load_passes():
    with open("./data/data05.txt") as f:
        X = f.read().split("\n")
    return X


def binary_search(chars: str, upper: int) -> int:
    lower = 0
    mid = (upper + lower) // 2
    for c in chars:
        if c == "F" or c == "L":
            upper = mid
        else:
            lower = mid
        mid = (upper + lower) // 2
    return mid


def get_row(s: str) -> int:
    return binary_search(s, 128)


def get_col(s: str) -> int:
    return binary_search(s, 8)


def get_seat_id(row: int, col: int) -> int:
    return row * 8 + col


def parse_boarding_pass(s: str) -> Tuple[int, int, int]:
    row = get_row(s[:-3])
    col = get_col(s[-3:])
    seat_id = get_seat_id(row, col)
    return seat_id


def parse_all_boarding_passes(X: List[str]) -> int:
    seat_ids = [parse_boarding_pass(s) for s in X]
    return max(seat_ids)


def find_my_own_seat(X: List[str]) -> int:
    sorted_seats = np.array(sorted([parse_boarding_pass(s) for s in X]))
    diff_seats = np.diff(sorted_seats)
    my_seat = sorted_seats[np.where(diff_seats == 2)[0][0]] + 1
    return my_seat


if __name__ == "__main__":
    X = load_passes()
    print(parse_all_boarding_passes(X))
    print(find_my_own_seat(X))
