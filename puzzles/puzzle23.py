from typing import List, Tuple, Union, Deque, Iterable, Dict
from collections import deque
from tqdm import tqdm  # type: ignore


def get_data(fn: str) -> Deque[int]:
    with open(fn) as f:
        data = f.read()
    return deque([int(el) for el in data])


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next: Union[None, Node] = None

    def __repr__(self) -> str:
        return str(self.value)


class CircularLinkedList:
    def __init__(self, data: Deque[int]) -> None:
        self.nodes: Dict[int, Node] = {}
        node = Node(data.popleft())
        self.head = node
        for value in data:
            node.next = Node(value)
            node = node.next
            self.nodes[value] = node
        node.next = self.head
        self.nodes[self.head.value] = self.head
        self.maxval = max(data)

    def traverse(self, start: Union[int, None] = None) -> Iterable[Node]:
        if start is not None:
            start_node = self.nodes[start]
        else:
            start_node = self.head
        node = start_node
        while node.next != start_node and node.next is not None:
            yield node
            node = node.next
        yield node

    def print_list(self, start: int = None):
        nodes = []
        for node in self.traverse(start):
            nodes.append(str(node))
        print(" -> ".join(nodes))

    def get_solution_str(self) -> str:
        nodes = []
        iter_node = self.traverse(1)
        _ = next(iter_node)
        for node in iter_node:
            nodes.append(str(node))
        return "".join(nodes)

    def pick_up(self):
        iter_node = self.traverse(self.head.value)
        _ = next(iter_node)
        nodes = []
        for _ in range(3):
            n = next(iter_node)
            nodes.append(n.value)

        # cut out the 3 nodes after head
        self.head.next = self.nodes[nodes[2]].next

        # find destination
        dest = self.head.value - 1 if self.head.value != 1 else self.maxval
        while dest in nodes:
            if dest == 1:
                dest = self.maxval
            else:
                dest -= 1

        # implement after destination node
        dest_next = self.nodes[dest].next
        self.nodes[dest].next = self.nodes[nodes[0]]
        self.nodes[nodes[2]].next = dest_next

        # set new head
        self.head = self.head.next


def solve_part1(fn: str) -> int:
    input = get_data(fn)
    cll = CircularLinkedList(data=input)
    for _ in range(100):
        cll.pick_up()
    return int(cll.get_solution_str())


def solve_part2(fn: str) -> int:
    input = get_data(fn)
    input = input + deque(range(max(input) + 1, 1_000_001))
    cll = CircularLinkedList(data=input)
    for _ in tqdm(range(10_000_000)):
        cll.pick_up()

    n1 = cll.nodes[1].next
    n2 = cll.nodes[n1.value].next
    return n1.value * n2.value


if __name__ == "__main__":

    fn = "./data/test_data23.txt"

    ans = solve_part1(fn)
    print("solution of part 1:", ans)

    ans2 = solve_part2(fn)
    print("solution of part 2:", ans2)

