from typing import List, Dict, Any
import unittest
from unittest import TestCase


def left(i: int) -> int:
    return 2 * i + 1


def right(i: int) -> int:
    return 2 * i + 2


def parent(i: int) -> int:
    """0, 1, 2, 3, 4, 5, 6, 7, 8
       ^  ^  ^
          ^     ^  ^
             ^        ^  ^

    The parent of 1 and 2 is 0
    The parent of 3 and 4 is 1
    The parent of 5 and 6 is 2
    The parent of 7 and 8 is 3
    """
    if i % 2 == 0:
        return (i // 2) - 1
    else:
        return i // 2


def min_heapify(A: List, i: int):
    l = left(i)
    r = right(i)
    heap_size = len(A) - 1

    if l <= heap_size and A[l] < A[i]:
        smallest = l
    else:
        smallest = i
    if r <= heap_size and A[r] < A[smallest]:
        smallest = r

    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        A = min_heapify(A, smallest)

    return A


def build_min_heap(A: List) -> List:
    heap_size = len(A) - 1
    mid_point = heap_size // 2
    for i in range(mid_point, -1, -1):
        min_heapify(A, i)

    return A


def heap_minimum(A: List) -> int:
    return A[0]


def heap_extract_min(A: List) -> List:
    heap_size = len(A) - 1
    if len(A) < 1:
        raise Exception("Heap underflow")
    min = A[0]
    A[0] = A[heap_size]
    del A[heap_size]
    min_heapify(A, 0)
    return min


def heap_decrease_key(A: List, i: int, key: int) -> List:
    if key > A[i]:
        raise Exception("New key is greater than current key.")
    A[i] = key
    while i > 0 and A[parent(i)] > A[i]:
        A[parent(i)], A[i] = A[i], A[parent(i)]
        i = parent(i)

    return A


def min_heap_insert(A: List, key: int) -> List:
    A.append(float("inf"))
    A = heap_decrease_key(A, len(A) - 1, key)
    return A


class TestMinPriorityQueue(TestCase):
    def test_left(self):
        self.assertEqual(left(0), 1)
        self.assertEqual(left(1), 3)
        self.assertEqual(left(2), 5)

    def test_right(self):
        self.assertEqual(right(0), 2)
        self.assertEqual(right(1), 4)
        self.assertEqual(right(2), 6)

    def test_parent(self):
        self.assertEqual(parent(1), 0)
        self.assertEqual(parent(2), 0)
        self.assertEqual(parent(3), 1)

    def test_build_min_heap(self):
        A = [4, 10, 3, 5, 1]
        self.assertEqual(build_min_heap(A), [1, 4, 3, 5, 10])

    def test_heap_minimum(self):
        A = [1, 3, 5]
        self.assertEqual(heap_minimum(A), 1)

    def test_heap_extract_min(self):
        A = [1, 3, 5, 7]
        self.assertEqual(heap_extract_min(A), 1)
        self.assertEqual(A, [3, 7, 5])

    def test_heap_decrease_key(self):
        A = [3, 5, 6, 9, 7]
        self.assertEqual(
            heap_decrease_key(A, 4, 1),
            [1, 3, 6, 9, 5],
        )

    def test_max_heap_insert(self):
        A = [1, 2, 3]
        self.assertEqual(min_heap_insert(A, 0), [0, 1, 3, 2])


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestMinPriorityQueue))
    runner = unittest.TextTestRunner()
    runner.run(suite)
