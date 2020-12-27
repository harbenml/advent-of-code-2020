from typing import Dict, List, Set, Tuple


def get_data(fn: str) -> Tuple[List[List[str]], List[List[str]]]:
    with open(fn) as f:
        data = f.read().strip().split("\n")

    foods = [el.split(" (contains ")[0].split(" ") for el in data]
    allergs = [el.split(" (contains ")[1].split(")")[0].split(", ") for el in data]
    return foods, allergs


def create_dict(
    foods: List[List[str]], allergs: List[List[str]]
) -> Dict[str, Set[str]]:
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
    return d


def identify_ingredients_with_allergens(d: Dict[str, Set[str]]) -> Dict[str, str]:
    identified = {}
    while True:
        allerg_with_single_ingred = [k for k, v in d.items() if len(v) == 1]
        if not allerg_with_single_ingred:
            break
        ingred_to_del = d[allerg_with_single_ingred[0]].pop()
        identified[allerg_with_single_ingred[0]] = ingred_to_del
        for v in d.values():
            if ingred_to_del in v:
                v.remove(ingred_to_del)
    return identified


def get_foods_without_allergens(foods: List, identified: Dict[str, str]) -> List[str]:
    foods_with_allergen = list(identified.values())
    food_without_allergen = [
        el for food in foods for el in food if el not in foods_with_allergen
    ]
    return food_without_allergen


def get_str_of_identified(identified: Dict[str, str]) -> str:
    ing = [identified[k] for k in sorted(identified)]
    return ",".join(ing)


def solve_part1(fn: str) -> Tuple[int, Dict[str, str]]:
    foods, allergs = get_data(fn)
    d = create_dict(foods, allergs)
    identified = identify_ingredients_with_allergens(d)
    food_without_allergen = get_foods_without_allergens(foods, identified)
    return len(food_without_allergen), identified


def solve_part2(identified: Dict[str, str]) -> str:
    """
    identified:

    'eggs': 'hn',
    'fish': 'dgsdtj',
    'nuts': 'kpksf',
    'peanuts': 'sjcvsr',
    'sesame': 'bstzgn',
    'shellfish': 'kmmqmv',
    'soy': 'vkdxfj',
    'wheat': 'bsfqgb'

    Solution:

    hn,dgsdtj,kpksf,sjcvsr,bstzgn,kmmqmv,vkdxfj,bsfqgb

    """
    ingreds = [identified[k] for k in sorted(identified)]
    return ",".join(ingreds)


if __name__ == "__main__":

    fn = "./data/test_data21.txt"
    ans1, identified = solve_part1(fn)
    ans2 = solve_part2(identified)
    print("solution part 1:", ans1)
    print("solution part 2:", ans2)
