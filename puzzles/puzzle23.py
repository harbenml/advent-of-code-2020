from typing import List, Tuple, Union, Deque, Iterable, Dict
from collections import deque


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

    def traverse(self, start: Union[int, None] = None) -> Iterable:
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

    def print_solution_str(self):
        nodes = []
        iter_node = self.traverse(1)
        _ = next(iter_node)
        for node in iter_node:
            nodes.append(str(node))
        print("".join(nodes))

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
        dest = self.head.value - 1 if self.head.value != 1 else 9
        while dest in nodes:
            if dest == 1:
                dest = 9
            else:
                dest -= 1

        # implement after destination node
        dest_next = self.nodes[dest].next
        self.nodes[dest].next = self.nodes[nodes[0]]
        self.nodes[nodes[2]].next = dest_next

        # set new head
        self.head = self.head.next

        # self.print_list()
        # print("hi")


input = deque([3, 8, 9, 1, 2, 5, 4, 6, 7])
cll = CircularLinkedList(data=input)
for _ in range(10):
    cll.pick_up()
cll.print_solution_str()

input = deque([3, 1, 8, 9, 4, 6, 5, 7, 2])
cll = CircularLinkedList(data=input)
for _ in range(100):
    cll.pick_up()
cll.print_solution_str()

