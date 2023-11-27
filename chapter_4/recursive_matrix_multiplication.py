from typing import List
import numpy as np
from numpy import ndarray


def square_even_matrix_multiplication(A: ndarray, B: ndarray) -> ndarray:
    if len(A) == 1 and len(A[0]) == 1:
        return np.array([[A[0, 0] * B[0, 0]]])

    mid = len(A) // 2
    A00 = A[0:mid, 0:mid]
    A01 = A[0:mid, mid:]
    A10 = A[mid:, 0:mid]
    A11 = A[mid:, mid:]

    B00 = B[0:mid, 0:mid]
    B01 = B[0:mid, mid:]
    B10 = B[mid:, 0:mid]
    B11 = B[mid:, mid:]

    # fmt: off
    C00 = square_even_matrix_multiplication(A00, B00) + square_even_matrix_multiplication(A01, B10)
    C01 = square_even_matrix_multiplication(A00, B01) + square_even_matrix_multiplication(A01, B11)
    C10 = square_even_matrix_multiplication(A10, B00) + square_even_matrix_multiplication(A11, B10)
    C11 = square_even_matrix_multiplication(A10, B01) + square_even_matrix_multiplication(A11, B11)
    # fmt: on

    C = np.vstack((np.hstack((C00, C01)), np.hstack((C10, C11))))
    return C


class UnitTestSquareEvenMatrixMultiplication:
    def test_all_multipliers(self) -> None:
        self.test1()
        self.test2()
        self.test4()

    def test1(self):
        self._test_matrix_multiplication(
            np.array(
                [
                    [1],
                ]
            ),
            np.array(
                [
                    [1],
                ]
            ),
            np.array(
                [
                    [1],
                ]
            ),
        )

    def test2(self):
        self._test_matrix_multiplication(
            np.array(
                [
                    [1, 2],
                    [3, 4],
                ]
            ),
            np.array(
                [
                    [1, 2],
                    [3, 4],
                ]
            ),
            np.array(
                [
                    [7, 10],
                    [15, 22],
                ]
            ),
        )

    def test4(self):
        self._test_matrix_multiplication(
            np.array(
                [
                    [1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 0, 1, 2],
                    [3, 4, 5, 6],
                ]
            ),
            np.array(
                [
                    [1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 0, 1, 2],
                    [3, 4, 5, 6],
                ]
            ),
            np.array(
                [
                    [50, 30, 40, 50],
                    [122, 78, 104, 130],
                    [24, 26, 38, 50],
                    [86, 54, 72, 90],
                ]
            ),
        )

    def _test_matrix_multiplication(
        self,
        matrix_1: ndarray,
        matrix_2: ndarray,
        expected: ndarray,
    ) -> None:
        actual = square_even_matrix_multiplication(matrix_1, matrix_2)
        assert np.array_equal(
            square_even_matrix_multiplication(matrix_1, matrix_2),
            expected,
        ), f"{actual}\n\n is not equal to \n\n{expected}"


UnitTestSquareEvenMatrixMultiplication().test_all_multipliers()
