from typing import Tuple, List, Callable


class Ferry1(object):
    def __init__(self) -> None:
        self.direction = go_east
        self.next_step = go_east
        self.position = [0, 0]

    def get_distance(self) -> int:
        return abs(self.position[0]) + abs(self.position[1])

    def do_step(self, value: int) -> None:
        self.position = self.next_step(self.position, value)

    def set_direction(self, action: str) -> None:
        if action == "N":
            self.next_step = go_north
        if action == "S":
            self.next_step = go_south
        if action == "E":
            self.next_step = go_east
        if action == "W":
            self.next_step = go_west
        if action == "F":
            self.next_step = self.direction

    def rotate_direction(self, action: str, value: int):
        dirs = [go_north, go_east, go_south, go_west]
        curr_dir_idx = dirs.index(self.direction)
        if action == "L":
            value *= -1
        self.direction = dirs[(curr_dir_idx + value // 90) % 4]

    def process_actions(self, actions: List) -> int:
        for action in actions:
            if action[0] in ["R", "L"]:
                self.rotate_direction(action[0], int(action[1:]))
            else:
                self.set_direction(action[0])
                self.do_step(int(action[1:]))
        return self.get_distance()


def go_north(pos: List, value: int) -> List:
    pos[0] += value
    return pos


def go_south(pos: List, value: int) -> List:
    pos[0] -= value
    return pos


def go_east(pos: List, value: int) -> List:
    pos[1] += value
    return pos


def go_west(pos: List, value: int) -> List:
    pos[1] -= value
    return pos


class Ferry2(object):
    def __init__(self):
        self.waypoint = [1, 10]
        self.position = [0, 0]

    def set_waypoint(self, action: str, value: int) -> None:
        if action == "N":
            self.waypoint[0] += value
        if action == "E":
            self.waypoint[1] += value
        if action == "S":
            self.waypoint[0] -= value
        if action == "W":
            self.waypoint[1] -= value
        if action in ["L", "R"]:
            if (action == "R" and value == 270) or (action == "L" and value == 90):
                self.waypoint = self.waypoint[::-1]
                self.waypoint[1] = -self.waypoint[1]
            if (action == "R" and value == 90) or (action == "L" and value == 270):
                self.waypoint = self.waypoint[::-1]
                self.waypoint[0] = -self.waypoint[0]
            if value == 180:
                self.waypoint[0] = -self.waypoint[0]
                self.waypoint[1] = -self.waypoint[1]

    def move_forward(self, value: int) -> None:
        self.position[0] += value * self.waypoint[0]
        self.position[1] += value * self.waypoint[1]

    def get_distance(self) -> int:
        return abs(self.position[0]) + abs(self.position[1])

    def process_actions(self, actions: List) -> int:
        for action in actions:
            if action[0] == "F":
                self.move_forward(int(action[1:]))
            else:
                self.set_waypoint(action[0], int(action[1:]))

        return self.get_distance()


if __name__ == "__main__":

    with open("./data/data12.txt") as f:
        actions = f.read().split("\n")

    # part 1
    boat = Ferry1()
    distance = boat.process_actions(actions)
    print(distance)

    # part2
    boat = Ferry2()
    distance = boat.process_actions(actions)
    print(distance)
