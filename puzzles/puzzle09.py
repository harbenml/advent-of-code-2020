def load_data(filename: str) -> list:
    with open(filename) as f:
        X = f.read().split("\n")
    X = [int(el) for el in X]
    return X


class Encoder(object):
    def __init__(self, buffer: list, buffer_size: int) -> None:
        self.buffer = buffer
        self.buffer_size = buffer_size

    def add_to_buffer(self, num: int) -> None:
        self.buffer.pop(0)
        self.buffer.append(num)

    def validate(self, num: int) -> bool:
        for i in range(self.buffer_size):
            for j in range(i + 1, self.buffer_size):
                if self.buffer[i] + self.buffer[j] == num:
                    return True
        return False


def find_contiguous_set(nums: list, target: int):
    for i in range(len(nums)):
        for j in range(i + 2, len(nums)):
            if sum(nums[i:j]) == target:
                return min(nums[i:j]) + max(nums[i:j])


def check_values(enc: Encoder, nums_to_check: list) -> int:
    for num in nums_to_check:
        if enc.validate(num):
            enc.add_to_buffer(num)
        else:
            return num
    return -1


if __name__ == "__main__":

    filename = "./data/data09.txt"
    input = load_data(filename)
    enc = Encoder(input[:25], 25)
    nums_to_check = input[25:]
    result = check_values(enc, nums_to_check)
    print(result)
    print(find_contiguous_set(input, result))
