from typing import List, Optional
import random

"""
In merge sort, we (1) recursively split the array into subarrays until the subarrays are
of size 1 and then we (2) merge the arrays back into the original array.

1) We need to recursively split the subarrays, keeping track of the indices of
the array that we're currently on.
2) Once we're done recursively splitting the subarrays


[ 90, 34, 5, 6, 7, 8, 1, 2, 3, 4, 34, 56]
[  0,  1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
          p        q           r
          n_1      n_2

"""


def merge(A: List, p: int, q: int, r: int) -> List:
    """Merge the two sorted subarrays"""
    n_1 = q - p + 1
    n_2 = r - q

    L, R = [], []
    for i in range(n_1):
        L.append(A[p + i])
    L.append(float("inf"))
    for i in range(n_2):
        R.append(A[q + 1 + i])
    R.append(float("inf"))

    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

    return A


def merge_sort(
    original_array: List,
    p: Optional[int] = None,
    r: Optional[int] = None,
) -> List:
    if p is None or r is None:
        p = 0
        r = len(original_array) - 1

    if p < r:
        q = (p + r) // 2
        merge_sort(original_array, p, q)
        merge_sort(original_array, q + 1, r)
        merge(original_array, p, q, r)

    return original_array


class MergeSortUnitTests:
    def run_all_tests(self):
        self.test_empty_list()
        self.test_single_element_list()
        self.test_merge_sort()
        self.test_merge_sort_reverse_sorted()
        self.test_merge_sort_random()

    def test_empty_list(self):
        assert merge_sort([]) == []

    def test_single_element_list(self):
        assert merge_sort([1]) == [1]

    def test_merge_sort(self):
        assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_merge_sort_reverse_sorted(self):
        assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_merge_sort_random(self):
        lst = [random.randint(1, 100) for _ in range(10)]
        assert merge_sort(lst) == sorted(lst)


MergeSortUnitTests().run_all_tests()
print(merge_sort([99999, 34, 243, 1, 45, 6, 7089]))
