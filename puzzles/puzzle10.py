import numpy as np
import pandas as pd


def load_data(filename: str) -> np.array:
    X = pd.read_csv(filename, header=None).values
    X = np.array(X)
    return X.reshape(-1)


def solve_part_1(X: np.array) -> int:
    X = sorted(X)
    X = np.insert(X, 0, 0)
    d = np.append(np.diff(X), 3)
    return sum(d == 1) * sum(d == 3)


def solve_part_2(X: np.array) -> int:
    # memoization
    memo = {}
    # Dynamic Programming
    def dp(i):
        if i == len(X) - 1:
            return 1
        if i in memo:
            return memo[i]
        result = 0
        for j in range(i + 1, len(X)):
            if X[j] - X[i] <= 3:
                result += dp(j)
        memo[i] = result
        return result

    return dp(0)


if __name__ == "__main__":
    filename = "./data/test_data10.txt"
    X = load_data(filename)
    print(solve_part_1(X))
    print(solve_part_2(X))

