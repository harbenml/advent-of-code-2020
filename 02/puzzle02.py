with open("data02.txt") as f:
    lines = f.readlines()

# emove whitespace characters like `\n` at the end of each line
lines = [x.strip() for x in lines]

# part one
valid_pws = 0
for line in lines:
    line = line.split()
    letter = line[1][0]
    mini, maxi = line[0].split("-")
    occurances = line[2].count(letter)
    if occurances >= int(mini) and occurances <= int(maxi):
        valid_pws += 1

print(valid_pws)

# part two
valid_pws = 0
for line in lines:
    line = line.split()
    letter = line[1][0]
    pos1, pos2 = line[0].split("-")
    l1, l2 = line[2][int(pos1) - 1], line[2][int(pos2) - 1]
    if int(l1 == letter) + int(l2 == letter) == 1:
        valid_pws += 1

print(valid_pws)
