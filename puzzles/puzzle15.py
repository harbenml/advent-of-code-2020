from typing import List


class Number(object):
    def __init__(self, value, pos):
        self.value = value
        self.pos = pos
        self.dist = 0

    def __repr__(self):
        return f"Number {self.value}, position {self.pos}, distance {self.dist}"


def solve(sequence: List[int], n: int) -> int:
    numbers = {val: Number(val, i + 1) for i, val in enumerate(sequence)}
    while len(sequence) < n:
        last_num = sequence[-1]
        if numbers[sequence[-1]].dist == 0 or last_num not in numbers:
            # last number has been spoken for the first time
            if 0 in numbers:
                numbers[0].dist = len(sequence) + 1 - numbers[0].pos
                numbers[0].pos = len(sequence) + 1
            else:
                numbers[0] = Number(0, len(sequence) + 1)
            sequence.append(0)
        elif numbers[sequence[-1]].dist != 0:
            # last number already exists
            sequence.append(numbers[last_num].dist)
            new_last_num = numbers[last_num].dist
            if new_last_num in numbers:
                numbers[new_last_num].dist = len(sequence) - numbers[new_last_num].pos
                numbers[new_last_num].pos = len(sequence)
            else:
                numbers[new_last_num] = Number(new_last_num, len(sequence))
    return numbers[sequence[-1]].value


if __name__ == "__main__":

    # puzzle input
    sequence = [9, 12, 1, 4, 17, 0, 18]

    # solution of part 1
    print(solve(sequence, 2020))

    # solution of part 2
    print(solve(sequence, 30000000))
