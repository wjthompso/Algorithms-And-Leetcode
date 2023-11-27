from typing import List, Dict, Any, Tuple
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


def insertion_sort(A: List[int], p: int, r: int) -> List:
    """
    Insertion sort algorithm, but we only sort the subarray A[p..r],
    not the entire array.
    """
    for i in range(p, r):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key
    return A


def select(A: List, p: int, r: int, i: int) -> int:
    """Return the ith smallest element in the array from section
    9.3 of Introduction to Algorithms, 3rd edition.

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
    # Divide the n elements of the input array into floor(n/5) groups of 5
    # elements each and at most one group made up of the remaining n mod 5
    # elements.
    if len(A) <= 5:
        insertion_sort(A, 0, len(A))
        return A[i - 1]

    medians = []
    for j in range(p, r + 1, 5):
        sub_right = min(j + 4, r)
        insertion_sort(A, j, sub_right)
        medians.append(A[j + (sub_right - j) // 2])

    median_of_medians: int = select(medians, 0, len(medians) - 1, (len(medians)) // 2)
    # Set the median of medians as the pivot
    pivot = A.index(median_of_medians, p, r + 1)
    A[pivot], A[r] = A[r], A[pivot]
    q = partition(A, p, r)

    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return select(A, p, q - 1, i)
    else:
        return select(A, q + 1, r, i - k)


# def select(A, p, r, i):
#     if r - p + 1 <= 5:
#         A[p : r + 1] = sorted(A[p : r + 1])
#         return A[p + i - 1]

#     for j in range(p, r + 1, 5):
#         sub_right = min(j + 4, r)
#         A[j : sub_right + 1] = sorted(A[j : sub_right + 1])
#         median_index = j + (sub_right - j) // 2
#         A[median_index], A[p + (j - p) // 5] = A[p + (j - p) // 5], A[median_index]

#     mid = (r - p) // 10 + p + 1
#     mom = select(A, p, p + (r - p) // 5, mid - p)
#     mom_index = A.index(mom, p, r + 1)
#     A[mom_index], A[r] = A[r], A[mom_index]
#     q = partition(A, p, r)

#     k = q - p + 1
#     if i == k:
#         return A[q]
#     elif i < k:
#         return select(A, p, q - 1, i)
#     else:
#         return select(A, q + 1, r, i - k)


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
        self.test_randomized_select_6()
        self.test_randomized_select_1()
        self.test_randomized_select_2()
        self.test_randomized_select_3()
        self.test_randomized_select_5()

    def test_randomized_select_1(self):
        assert select([3, 1, 4, 1, 5, 9, 2, 6], 0, 7, 1) == 1

    def test_randomized_select_2(self):
        assert select([3, 1, 4, 1, 5, 9, 2, 6], 0, 7, 2) == 1

    def test_randomized_select_3(self):
        actual = select([3, 1, 4, 1, 5, 9, 2, 6], 0, 7, 3)
        expected = 2
        assert actual == expected, f"Expected {expected}, got {actual}"

    def test_randomized_select_4(self):
        actual = select([3, 1, 4, 1, 5, 9, 2, 6], 0, 7, 4)
        expected = 3
        assert actual == expected, f"Expected {expected}, got {actual}"

    def test_randomized_select_5(self):
        assert select([3, 1, 4, 1, 5, 9, 2, 6], 0, 7, 5) == 4

    def test_randomized_select_6(self):
        assert select([0, 3, 676, 34, 12], 0, 4, 3) == 12


if __name__ == "__main__":
    UnitTester().run_all_tests()
