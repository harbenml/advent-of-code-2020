with open("./data/test_data13.txt") as f:
    lines = f.read().split("\n")

departure = int(lines[0])
bus_ids = lines[1].split(",")

delays = [i for i, el in enumerate(bus_ids) if not el == "x"]
print(delays)

bus_ids = [int(el) for el in bus_ids if not el == "x"]

wait_time = [(departure // el + 1) * el - departure for el in bus_ids]
best_bus_id = bus_ids[wait_time.index(min(wait_time))]

print(bus_ids)
print(wait_time)
print(best_bus_id)
print(best_bus_id * min(wait_time))


"""
- How many minutes delay between the busses?
- Start with the bus that has the highest bus ID
- Search the bus with the next lower bus ID
- What is the desired delay time between these two busses?
"""
