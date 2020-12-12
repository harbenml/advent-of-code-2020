from typing import Tuple
from typing import Callable


def check_single_seat(value: "str") -> int:
    if value == "L":
        return 0
    if value == "#":
        return 1
    return 0


def check_adjacent_seats(X: list, row: int, col: int) -> int:
    nrows, ncols = len(X), len(X[0])
    if X[row][col] == ".":
        return 0
    occupied = 0
    for i in range(max(row - 1, 0), min(nrows, row + 2)):
        for j in range(max(col - 1, 0), min(ncols, col + 2)):
            if not (i == row and j == col):
                occupied += check_single_seat(X[i][j])
    return occupied


def check_visible_seats(X: list, row: int, col: int) -> int:
    if X[row][col] == ".":
        return 0
    occupied = 0
    occupied += check_horizontal(X, row, col)
    occupied += check_vertical(X, row, col)
    occupied += check_diagonal(X, row, col)
    return occupied


def check_horizontal(X, row, col):
    ncols = len(X[0])
    count = 0
    # go right
    for j in range(col + 1, ncols):
        if X[row][j] == "#" or X[row][j] == "L":
            if X[row][j] == "#":
                count += 1
            break
    # go left
    for j in range(col - 1, -1, -1):
        if X[row][j] == "#" or X[row][j] == "L":
            if X[row][j] == "#":
                count += 1
            break
    return count


def check_vertical(X, row, col):
    nrows = len(X)
    count = 0
    # go down
    for i in range(row + 1, nrows):
        if X[i][col] == "#" or X[i][col] == "L":
            if X[i][col] == "#":
                count += 1
            break
    # go up
    for i in range(row - 1, -1, -1):
        if X[i][col] == "#" or X[i][col] == "L":
            if X[i][col] == "#":
                count += 1
            break
    return count


def check_diagonal(X, row, col):
    nrows, ncols = len(X), len(X[0])
    count = 0
    # go down right
    i, j = row, col
    while i < nrows - 1 and j < ncols - 1:
        i += 1
        j += 1
        if X[i][j] == "#" or X[i][j] == "L":
            if X[i][j] == "#":
                count += 1
            break
    # go up left
    i, j = row, col
    while i > 0 and j > 0:
        i -= 1
        j -= 1
        if X[i][j] == "#" or X[i][j] == "L":
            if X[i][j] == "#":
                count += 1
            break
    # go up right
    i, j = row, col
    while i > 0 and j < ncols - 1:
        i -= 1
        j += 1
        if X[i][j] == "#" or X[i][j] == "L":
            if X[i][j] == "#":
                count += 1
            break
    # go down left
    i, j = row, col
    while i < nrows - 1 and j > 0:
        i += 1
        j -= 1
        if X[i][j] == "#" or X[i][j] == "L":
            if X[i][j] == "#":
                count += 1
            break
    return count


def run_algorithm(
    X: list, check_seats: Callable, num_seats_to_check: int
) -> Tuple[list, int]:
    nrows, ncols = len(X), len(X[0])
    X_new = X.copy()
    count_all_occupied = 0
    for i in range(nrows):
        for j in range(ncols):
            occupied = check_seats(X, i, j)
            if X[i][j] == "L" and occupied == 0:
                X_new[i] = X_new[i][:j] + "#" + X_new[i][j + 1 :]
            elif X[i][j] == "#" and occupied >= num_seats_to_check:
                X_new[i] = X_new[i][:j] + "L" + X_new[i][j + 1 :]
            if X_new[i][j] == "#":
                count_all_occupied += 1
    return X_new, count_all_occupied


def solve(X: list, fun: Callable, num_seats_to_check: int) -> Tuple[list, int]:
    occupied_seats = [0]
    for _ in range(100):
        X, count = run_algorithm(X, fun, num_seats_to_check)
        occupied_seats.append(count)
        if occupied_seats[-1] - occupied_seats[-2] == 0:
            print(count)
            break
    return X, count


if __name__ == "__main__":

    with open("./data/data11.txt") as f:
        X = f.read().split("\n")

    # solve part 1
    solve(X, check_adjacent_seats, 4)

    # solve part 2
    solve(X, check_visible_seats, 5)

