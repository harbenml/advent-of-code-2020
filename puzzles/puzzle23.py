from typing import List, Tuple, Union, Deque, Iterable


class Node:
    def __init__(self, value: int = None):
        self.value = value
        self.next: Union[None, Node] = None

    def __repr__(self) -> str:
        return str(self.value)


class CircularLinkedList:
    """
    Implementation of a circular linked list according to the great
    tutorial at https://realpython.com/linked-lists-python/
    """

    def __init__(self, data: Deque[int]) -> None:
        self.head: Union[None, Node] = None
        if data:
            node = Node(data.popleft())
            self.head = node
            for value in data:
                node.next = Node(value)
                node = node.next
            node.next = self.head

    def traverse(self, start: int = None) -> Iterable:
        if start is None:
            start = self.head
        node = start
        while node is not None and (node != start):
            yield node
            node = node.next
        yield node

