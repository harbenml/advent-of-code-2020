import pandas as pd
import numpy as np

# part one
def solve_part_1(data: np.ndarray) -> int:
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] + data[j] == 2020:
                return int(data[i] * data[j])
    return -1


# part two
def solve_part_2(data: np.ndarray) -> int:
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            for k in range(j + 1, len(data)):
                if data[i] + data[j] + data[k] == 2020:
                    return int(data[i] * data[j] * data[k])
    return -1


if __name__ == "__main__":

    data = pd.read_csv("./data/data01.txt").values
    print(solve_part_1(data))
    print(solve_part_2(data))
