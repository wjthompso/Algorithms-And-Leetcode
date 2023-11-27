from typing import List
import random


def bubble_sort(A: List) -> List:
    for i in range(len(A)):
        for j in range(len(A) - 1, i, -1):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
    return A


class TestBubbleSort:
    def run_all_tests(self):
        self.test_empty_list()
        self.test_single_element_list()
        self.test_sorted_list()
        self.test_reverse_sorted_list()
        self.test_random_list()

    def test_empty_list(self):
        assert bubble_sort([]) == []

    def test_single_element_list(self):
        assert bubble_sort([1]) == [1]

    def test_sorted_list(self):
        assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_reverse_sorted_list(self):
        assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_random_list(self):
        lst = [random.randint(1, 100) for _ in range(10)]
        assert bubble_sort(lst) == sorted(lst)


TestBubbleSort().run_all_tests()
