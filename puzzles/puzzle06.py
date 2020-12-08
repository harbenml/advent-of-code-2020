from typing import List, Tuple


def load_data(filename: str) -> Tuple[List, List]:
    with open(filename) as f:
        X = f.read().split("\n\n")
    no_people = [el.count("\n") + 1 for el in X]
    X = [el.replace("\n", "") for el in X]
    X_unique = ["".join(set(el)) for el in X]
    return X, X_unique, no_people


def get_sum_of_counts(X: List, X_unique: List) -> int:
    X_unique_sum = sum([len(el) for el in X_unique])
    return X_unique_sum


def get_sum_of_counts_everyone(X: List, X_unique: List, no_people: List) -> int:
    counts = 0
    for i, n in enumerate(no_people):
        counts += sum([X[i].count(el) == n for el in X_unique[i]])
    return counts


if __name__ == "__main__":

    filename = "./data/data06.txt"

    X, X_unique, no_people = load_data(filename)
    X_unique_sum = get_sum_of_counts(X, X_unique)
    counts = get_sum_of_counts_everyone(X, X_unique, no_people)
    print(X_unique_sum)
    print(counts)
