from build_max_heap import max_heapify, build_max_heap
from typing import List


def heapsort(A: List) -> List:
    A = build_max_heap(A)
    for i in range(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        A = max_heapify(A, i - 1, 0)

    return A


class TestHeapSort:
    def run_all_tests(self) -> None:
        self.run_test_2()
        self.run_test_1()
        self.run_test_3()
        self.run_test_4()
        self.run_test_5()
        self.run_test_6()
        self.run_test_7()
        self.run_test_8()

    def run_test_1(self) -> None:
        assert heapsort([1]) == [1]

    def run_test_2(self) -> None:
        assert heapsort([1, 2]) == [1, 2]

    def run_test_3(self) -> None:
        assert heapsort([2, 1]) == [1, 2]

    def run_test_4(self) -> None:
        assert heapsort([1, 2, 3]) == [1, 2, 3]

    def run_test_5(self) -> None:
        assert heapsort([3, 2, 1]) == [1, 2, 3]

    def run_test_6(self) -> None:
        assert heapsort([1, 2, 3, 4]) == [1, 2, 3, 4]

    def run_test_7(self) -> None:
        assert heapsort([4, 3, 2, 1]) == [1, 2, 3, 4]

    def run_test_8(self) -> None:
        assert heapsort([10, 1, 9, 2, 8, 3, 7, 4, 6, 5]) == [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
        ]


TestHeapSort().run_all_tests()
