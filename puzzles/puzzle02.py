def load_data():
    with open("./data/data02.txt") as f:
        lines = f.readlines()

    # remove whitespace characters like `\n` at the end of each line
    lines = [x.strip() for x in lines]
    return lines


def solve_part_1(lines: list) -> int:
    # part one
    valid_pws = 0
    for line in lines:
        line = line.split()
        letter = line[1][0]
        mini, maxi = line[0].split("-")
        occurances = line[2].count(letter)
        if occurances >= int(mini) and occurances <= int(maxi):
            valid_pws += 1
    return valid_pws


def solve_part_2(lines: list) -> int:
    # part two
    valid_pws = 0
    for line in lines:
        line = line.split()
        letter = line[1][0]
        pos1, pos2 = line[0].split("-")
        l1, l2 = line[2][int(pos1) - 1], line[2][int(pos2) - 1]
        if int(l1 == letter) + int(l2 == letter) == 1:
            valid_pws += 1
    return valid_pws


if __name__ == "__main__":

    lines = load_data()
    valid_pws1 = solve_part_1(lines)
    print(valid_pws1)

    valid_pws2 = solve_part_2(lines)
    print(valid_pws2)
