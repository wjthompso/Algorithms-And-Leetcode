from typing import List, Optional, Tuple
import random


def find_max_crossing_subarray(
    A: List[int], low: int, mid: int, high: int
) -> Tuple[int, int, int]:
    """Starting at a mid point, you're finding the largest
    contiguous subarray that crosses the midpoint."""
    left_sum = float("-inf")
    summ = 0
    max_left = mid
    for i in range(mid, low - 1, -1):
        summ += A[i]
        if summ > left_sum:
            left_sum = summ
            max_left = i
    right_sum = float("-inf")
    summ = 0
    max_right = mid + 1
    for j in range(mid + 1, high + 1):
        summ += A[j]
        if summ > right_sum:
            right_sum = summ
            max_right = j
    return (max_left, max_right, left_sum + right_sum)


def find_maximum_subarray(A: List[int], low: int, high: int) -> Tuple[int, int, int]:
    if high == low:
        # Base case of list size 1, return: We've split the array into two
        # arrays of one element
        return (low, high, A[low])
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = find_maximum_subarray(A, low, mid)
        right_low, right_high, right_sum = find_maximum_subarray(A, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)
        if left_sum >= cross_sum and left_sum >= right_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= cross_sum and right_sum >= left_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)


def find_maximum_subarray_wrapper(A: List[int]) -> Optional[List[int]]:
    """Given an array of numbers, find the maximum subarray of consecutive
    numbers. That is, find the subarray with the largest sum."""
    low = 0
    high = len(A) - 1
    low, high, max_sum = find_maximum_subarray(A, low, high)
    return A[low : high + 1]


def find_maximum_subarray_wrapper(A: List[int]) -> Optional[List[int]]:
    """This approach takes the idea that if you iterate straight through,
    summing as you go, and your sum goes negative, you should start a new
    contiguous array because your current negative sum will just bring down any
    sum you come up with moving forward. You can save the best array from the
    previous run, and then start looking for the best array you can find in the
    new numbers."""
    max_sum = A[0]
    curr_sum = 0
    curr_low = max_low = max_high = 0

    for i in range(len(A)):
        if curr_sum < 0:
            curr_sum = 0
            curr_low = i
        curr_high = i
        curr_sum += A[i]
        if curr_sum > max_sum:
            max_low = curr_low
            max_high = curr_high
            max_sum = curr_sum

    return A[max_low : max_high + 1]


class UnitTestMaximumSubarray:
    def run_all_tests(self) -> None:
        self.test_specific_example_2()
        self.test_single_element_list()
        self.test_sorted_list()
        self.test_reverse_sorted_list()
        self.test_random_list()
        self.test_specific_example_1()

    def test_single_element_list(self) -> None:
        assert find_maximum_subarray_wrapper([1]) == [1]

    def test_sorted_list(self) -> None:
        assert find_maximum_subarray_wrapper([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_reverse_sorted_list(self) -> None:
        assert find_maximum_subarray_wrapper([5, 4, 3, 2, 1]) == [5, 4, 3, 2, 1]

    def test_random_list(self) -> None:
        lst = [random.randint(1, 100) for _ in range(10)]
        assert find_maximum_subarray_wrapper(lst) == lst

    def test_specific_example_1(self) -> None:
        list = [-20, -40, 10, 20, 40, -10]
        assert find_maximum_subarray_wrapper(list) == [10, 20, 40]

    def test_specific_example_2(self) -> None:
        list = [-2, -1]
        assert find_maximum_subarray_wrapper(list) == [-1]


unit_tests = UnitTestMaximumSubarray().run_all_tests()
