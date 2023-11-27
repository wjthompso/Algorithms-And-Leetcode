from typing import List, Dict, Any
from unittest import TestCase
import random


def partition(A: List, p: int, r: int) -> int:
    """An implementation of the partition algorithm from section 7.1 of
    Introduction to Algorithms, 3rd edition."""
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def randomized_partition(A: List, p: int, r: int) -> int:
    """An implementation of the randomized partition algorithm from
    section 7.3 of Introduction to Algorithms, 3rd edition."""
    i: int = random.randint(p, r)
    A[r], A[i] = A[i], A[r]
    return partition(A, p, r)


def randomized_select(A: List, p: int, r: int, i: int) -> int:
    """Return the ith smallest element in the array from section
    9.2 of Introduction to Algorithms, 3rd edition.

    Arguments
    ---------

    A: List
        The list to be sorted.
    p: int
        The start index to sort from.
    r: int
        The end index to sort to.
    i: int
        The ith smallest element to return.

    Returns
    -------

    A[i]: int
        The ith smallest element in the array.

    """
    if p == r:
        return A[p]
    q = randomized_partition(A, p, r)
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return randomized_select(A, p, q - 1, i)
    else:
        return randomized_select(A, q + 1, r, i - k)


class UnitTester(TestCase):
    def run_all_tests(self):
        """Run all defined tests in the class."""
        # Write code here that finds all of the tests defined in the class that
        # are not private (i.e. do not start with an underscore) and are not the
        # current method and runs them.
        # method_names = [
        #     method for method in dir(self) if callable(getattr(self, method))
        # ]

        # test_methods = [
        #     method
        #     for method in method_names
        #     if method.startswith("test_") and method != "run_all_tests"
        # ]

        # # Run each test method
        # for method in test_methods:
        #     getattr(self, method)()

        self.test_randomized_select_4()
        self.test_randomized_select_1()
        self.test_randomized_select_2()
        self.test_randomized_select_3()
        self.test_randomized_select_5()

    def test_randomized_select_1(self):
        assert randomized_select([3, 1, 4, 1, 5, 9, 2, 6], 0, 7, 1) == 1

    def test_randomized_select_2(self):
        assert randomized_select([3, 1, 4, 1, 5, 9, 2, 6], 0, 7, 2) == 1

    def test_randomized_select_3(self):
        actual = randomized_select([3, 1, 4, 1, 5, 9, 2, 6], 0, 7, 3)
        expected = 2
        assert actual == expected, f"Expected {expected}, got {actual}"

    def test_randomized_select_4(self):
        actual = randomized_select([3, 1, 4, 1, 5, 9, 2, 6], 0, 7, 4)
        expected = 3
        assert actual == expected, f"Expected {expected}, got {actual}"

    def test_randomized_select_5(self):
        assert randomized_select([3, 1, 4, 1, 5, 9, 2, 6], 0, 7, 5) == 4


if __name__ == "__main__":
    UnitTester().run_all_tests()
