fn = "./data/data21.txt"
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


identified = {}
while True:
    allerg_with_single_ingred = [k for k, v in d.items() if len(v) == 1]
    if not allerg_with_single_ingred:
        break
    ingred_to_del = d[allerg_with_single_ingred[0]].pop()
    identified[allerg_with_single_ingred[0]] = ingred_to_del
    for k, v in d.items():
        if ingred_to_del in v:
            v.remove(ingred_to_del)
print(identified)

foods_with_allergen = list(identified.values())
food_without_allergen = [
    el for food in foods for el in food if el not in foods_with_allergen
]
print(len(food_without_allergen))
