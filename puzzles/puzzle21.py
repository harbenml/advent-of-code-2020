fn = "./data/test_data21.txt"
with open(fn) as f:
    data = f.read().strip().split("\n")

print(data)

foods = [el.split(" (contains ")[0].split(" ") for el in data]
print(foods)

allergs = [el.split(" (contains ")[1].split(")")[0].split(", ") for el in data]
print(allergs)

d = {}
idx = -1
for food in foods:
    idx += 1
    for al in allergs[idx]:
        print(al, food)
        if al not in d:
            d[al] = set(food)
        else:
            d[al] = d[al] & set(food)
print(d)
