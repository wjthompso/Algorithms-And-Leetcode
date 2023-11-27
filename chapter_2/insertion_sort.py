

import random
import unittest
from typing import List

def insertion_sort(A: List[int]) -> List:
    """
    Insertion sort algorithm
    """
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key
    return A

    

class TestSortingAlgorithm(unittest.TestCase):
    def run_all_tests(self):
        self.test_reverse_insertion_sorted_list()
        self.test_empty_list()
        self.test_single_element_list()
        self.test_insertion_sorted_list()
        self.test_random_list()

    def test_empty_list(self):
        self.assertEqual(insertion_sort([]), [])
        
    def test_single_element_list(self):
        self.assertEqual(insertion_sort([1]), [1])
        
    def test_insertion_sorted_list(self):
        self.assertEqual(insertion_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        
    def test_reverse_insertion_sorted_list(self):
        self.assertEqual(insertion_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        
    def test_random_list(self):
        lst = [random.randint(1, 100) for _ in range(10)]
        self.assertEqual(insertion_sort(lst), sorted(lst))

TestSortingAlgorithm().run_all_tests()