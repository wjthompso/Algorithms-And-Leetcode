from typing import List, Dict, Any
from unittest import TestCase


def quicksort(A: List, p: int, r: int) -> List:
    """An implementation of the quicksort algorithm from Introduction to
    Algorithms, 3rd edition, page 171.

    Arguments
    ---------

    A: List
        The list to be sorted.
    p: int
        The start index to sort from.
    r: int
        The end index to sort to.
    """
    if p < r:
        q = partition(A, p, r)
        A = quicksort(A, p, q - 1)
        A = quicksort(A, q + 1, r)

    return A


def partition(A: List, p: int, r: int) -> int:
    """An implementation of the partition algorithm from Introduction to
    Algorithms, 3rd edition, page 171.

    Notes: x is the pivot element. i is the index of the smaller element.
    j is the index of the element being compared to the pivot element.
    When the function returns, the subarray is partitioned into two
    subarrays, one with elements smaller than the pivot and one with
    elements larger than the pivot.

    Arguments
    ---------

    A: List
        The list to be sorted.
    p: int
        The start index to sort from.
    r: int
        The end index to sort to.

    Returns
    -------

    i + 1: int
        The index of the pivot element.
    """
    x: int = A[r]
    i: int = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


# Your quicksort and partition functions go here


class TestQuicksort(TestCase):
    def run_all_tests(self):
        """Run all defined tests in the class, e.g., tests which start with the
        word "test_" and are not the current method."""
        method_names = [
            method for method in dir(self) if callable(getattr(self, method))
        ]

        test_methods = [
            method
            for method in method_names
            if method.startswith("test_") and method != "run_all_tests"
        ]
        test_methods.sort()

        # Run each test method
        for method in test_methods:
            getattr(self, method)()

    def test_1_quicksort_sorts_list(self):
        assert quicksort([3, 1, 4, 1, 5, 9, 2, 6], 0, 7) == [1, 1, 2, 3, 4, 5, 6, 9]

    def test_2_quicksort_sorts_list(self):
        assert quicksort([9, 1, 11, 3, 17]) == [1, 3, 9, 11, 17]

    def test_quicksort_empty_list(self):
        assert quicksort([], 0, -1) == []

    def test_quicksort_single_element(self):
        assert quicksort([1], 0, 0) == [1]

    def test_quicksort_repeated_elements(self):
        assert quicksort([2, 2, 2, 2], 0, 3) == [2, 2, 2, 2]

    def test_partition(self):
        A = [3, 1, 4, 1, 5, 9, 2, 6]
        pivot_index = partition(A, 0, 7)
        pivot = A[pivot_index]
        left_subarray = A[:pivot_index]
        right_subarray = A[pivot_index + 1 :]
        assert all(x <= pivot for x in left_subarray)
        assert all(x > pivot for x in right_subarray)


if __name__ == "__main__":
    test = TestQuicksort()
    test.run_all_tests()
