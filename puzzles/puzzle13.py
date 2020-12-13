from typing import Tuple


def get_data(filename: str) -> Tuple[int, list, list]:
    with open(filename) as f:
        lines = f.read().split("\n")

    departure = int(lines[0])
    bus_ids = lines[1].split(",")
    delays = [i for i, el in enumerate(bus_ids) if not el == "x"]
    bus_ids = [int(el) for el in bus_ids if not el == "x"]
    return departure, bus_ids, delays


def solve_part_1(bus_ids: list, departure: int) -> int:
    wait_time = [(departure // el + 1) * el - departure for el in bus_ids]
    best_bus_id = bus_ids[wait_time.index(min(wait_time))]
    return best_bus_id * min(wait_time)


def solve_part_2(bus_ids: list, departure: int, delays: list) -> int:
    delta_time = 1
    timestamp = 0
    for bus, delay in list(zip(bus_ids, delays)):
        while (timestamp + delay) % bus != 0:
            timestamp += delta_time
        delta_time *= bus
    return timestamp


if __name__ == "__main__":

    departure, bus_ids, delays = get_data("./data/data13.txt")

    result1 = solve_part_1(bus_ids, departure)
    print("Solution part 1: ", result1)

    result2 = solve_part_2(bus_ids, departure, delays)
    print("Solution part 2: ", result2)
