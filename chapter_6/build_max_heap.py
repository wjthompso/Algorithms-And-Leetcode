from typing import List


def max_heapify(A: List, N: int, i: int) -> List:
    """Max-heapify the subtree rooted at index i. This assumes you've inserted
    an element and want to trickle it down the tree."""
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child <= N and A[left_child] > A[i]:
        largest = left_child
    else:
        largest = i
    if right_child <= N and A[right_child] > A[largest]:
        largest = right_child

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, N, largest)

    return A


def build_max_heap(A: List) -> List:
    heap_size = len(A) - 1
    mid_point = heap_size // 2
    for i in range(mid_point, -1, -1):
        max_heapify(A, heap_size, i)

    return A


class BuildMaxHeap:
    def run_all_tests(self) -> None:
        self.test4()
        self.test3()
        self.test1()
        self.test2()
        self.test5()

    def test1(self):
        assert build_max_heap([1]) == [1]

    def test2(self):
        assert build_max_heap([1, 2]) == [2, 1]

    def test3(self):
        assert build_max_heap([1, 2, 3]) in [[3, 2, 1], [3, 1, 2]]

    def test4(self):
        assert build_max_heap([1, 2, 3, 4]) in [[4, 3, 2, 1], [4, 2, 3, 1]]

    def test5(self):
        assert build_max_heap([1, 2, 3, 4, 5]) in [[5, 4, 3, 2, 1], [5, 4, 3, 1, 2]]


# BuildMaxHeap().run_all_tests()
