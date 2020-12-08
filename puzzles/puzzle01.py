import pandas as pd

data = pd.read_csv("./data/data01.txt").values

# part one
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if data[i] + data[j] == 2020:
            print(data[i] * data[j])

# part two
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        for k in range(j + 1, len(data)):
            if data[i] + data[j] + data[k] == 2020:
                print(data[i] * data[j] * data[k])
