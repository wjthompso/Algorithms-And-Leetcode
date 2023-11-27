from typing import List


# Implementation using low < high
def binary_search(A: List, target: int) -> int:
    """
    Binary search algorithm for a sorted list. If target
    in list, return the index of the target. Otherwise,
    return -1.
    """
    low = 0
    high = len(A)  # the low < high bool means high doesn't get considered

    while low < high:  # high is an exclusive upper bound: high doesn't get considered
        mid = (high + low) // 2
        if A[mid] == target:
            return mid
        elif A[mid] < target:
            low = mid + 1
        else:
            high = mid  # since high never gets considered, remove the mid - 1 otherwise we may skip values as we zoom in from the right

    return -1


# Implementation using low <= high
def binary_search(A: List, target: int) -> int:
    """
    Binary search algorithm for a sorted list. If target
    in list, return the index of the target. Otherwise,
    return -1.
    """
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (high + low) // 2
        if A[mid] == target:
            return mid
        elif A[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def binary_search(A: List, target: int) -> int:
    """
    Binary search algorithm for a sorted list. If target
    in list, return the index of the target. Otherwise,
    return -1.
    """
    low, high = 0, len(A) - 1

    while low <= high:
        mid = (low + high) // 2
        if A[mid] == target:
            return mid
        if A[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


class BinarySearchUnitTests:
    def run_all_tests(self):
        self.test_edge_case_2()
        self.test_edge_case_1()
        self.test_empty_list()
        self.test_single_element_list()
        self.test_binary_search()
        self.test_binary_search_not_found()

    def test_empty_list(self):
        self.assertEqual(binary_search([], 1), -1)

    def test_single_element_list(self):
        self.assertEqual(binary_search([1], 1), 0)

    def test_binary_search(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)

    def test_binary_search_beginning(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 1), 0)

    def test_binary_search_end(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 5), 4)

    def test_binary_search_not_found(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), -1)

    def test_edge_case_1(self):
        self.assertEqual(binary_search([2, 5], 5), 1)

    def test_edge_case_2(self):
        self.assertEqual(binary_search([-1, 0, 3, 5, 9, 12], 9), 4)

    def assertEqual(self, result, expected):
        assert result == expected, f"{result} != {expected}"


BinarySearchUnitTests().run_all_tests()
