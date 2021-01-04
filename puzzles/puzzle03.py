import numpy as np  # type: ignore


def load_data(filename: str) -> np.array:
    with open(filename) as f:
        X = f.readlines()
    # remove \n at end of line
    X = [x.strip() for x in X]
    return np.array(X, dtype=np.str)


def do_step_right(pos: int, step: int, width: int) -> int:
    """Takes current position and do 3 steps to the 
    right. Be aware of overflow as the board limit 
    on the right is reached."""
    new_pos = (pos + step) % width
    return new_pos


def do_step_down(pos: int, step: int, height: int) -> int:
    new_pos = pos + step
    if new_pos >= height:
        return -1
    else:
        return new_pos


def count_trees(X: np.array, step_right: int, step_down: int) -> int:
    no_trees = col = row = 0
    height, width = X.size, len(X[0])
    while row >= 0:
        if X[row][col] == "#":
            no_trees += 1
        col = do_step_right(col, step_right, width)
        row = do_step_down(row, step_down, height)

    return no_trees


if __name__ == "__main__":

    # filename = "./data/test_data03.txt"
    filename = "./data/data03.txt"
    X = load_data(filename)

    """
    List of moves:

    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.
    """
    moves = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    multi = 1
    for move in moves:
        multi *= count_trees(X, *move)
        print(count_trees(X, *move))

    print(multi)
