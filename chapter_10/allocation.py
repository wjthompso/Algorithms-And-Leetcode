from typing import List, Union, Any, Optional
from unittest import TestCase

"""This is a partial implementation of the single array linked list from CLRS 10.2.

It demonstrates how allocation and deallocation of nodes can be done in a single array
using the next and previous slots of each node to point to the next and previous nodes
in the list.

There are essentially two linked lists, one singly linked list for the free list and
a doubly linked list for the list of allocated nodes.
"""


class SingleArrayLinkedList:
    def __init__(self, size: int) -> None:
        self.array: List[int] = [None] * (size * 3)
        for i in range(0, (size - 1) * 3, 3):
            self.array[i + 1] = i + 3
        self.free = 0
        self.head: int = None
        self.tail: int = None
        self.allocated_nodes: int = 0

    def set_next(self, x: int, value: int) -> Optional[int]:
        """Given the index of a key in the array, set the value of the next slot
        for this index to the value of the next slot in the array."""
        if x is not None:
            self.array[x + 1] = value
        return None

    def set_prev(self, x: int, value: int) -> Optional[int]:
        """Given the index of a key in the array, set the value of the previous
        slot for this index to the value of the previous slot in the array."""
        if x is not None:
            self.array[x + 2] = value
        return None

    def get_next(self, x: int) -> Optional[int]:
        """Given the index of a key in the array, return the index of the next
        node which that node is pointing to."""
        if x is not None:
            return self.array[x + 1]
        return None

    def get_prev(self, x: int) -> int:
        """Given the index of a key in the array, return the index of the
        previous node which that node is pointing to."""
        if x is not None:
            return self.array[x + 2]
        return None

    def allocate_object(self) -> Optional[int]:
        """Return the index of the next free node in the free list, if one is
        available."""
        if self.free is None:
            raise Exception("Out of space")
        x = self.free
        self.free = self.get_next(self.free)
        return x

    def free_object(self, x: int) -> None:
        """Add the node at index x to the free list."""
        self.set_next(x, self.free)
        self.free = x

    def insert(self, key: int) -> None:
        """Insert a new node at the tail of the list with the value of key."""
        if self.head is None:
            x: int = self.allocate_object()
            self.head = self.tail = x
            self.allocated_nodes += 1
            self.array[x] = key
            return

        x = self.allocate_object()
        self.array[x] = key
        self.set_prev(x, self.tail)
        self.tail = x
        self.allocated_nodes += 1
        return

    def remove_from_tail(self) -> None:
        """Remove the node at the tail of the list and add it to the free list."""
        self.tail = self.array[self.tail + 2]
        self.allocated_nodes -= 1
        self.free_object(self.tail)


class UnitTester(TestCase):
    def run_all_tests(self):
        """Run all defined tests in the class."""
        self.test_1()

    def test_1(self):
        """Test the stack code."""
        single_linked_list: SingleArrayLinkedList = SingleArrayLinkedList(5)
        single_linked_list.insert(1)
        single_linked_list.insert(2)
        assert single_linked_list.allocated_nodes == 2
        single_linked_list.remove_from_tail()
        single_linked_list.remove_from_tail()
        assert single_linked_list.allocated_nodes == 0


if __name__ == """__main__""":
    tester = UnitTester()
    tester.run_all_tests()
