from typing import Union, Any, Optional
import unittest


def cut_rod(p: list, n: int) -> int:
    """Returns the maximum revenue for a rod of length n."""
    if n == 0:
        return 0
    q = -1
    for i in range(1, n + 1):
        q = max(q, p[i] + cut_rod(p, n - i))
    return q


# Top-down approach: recursive with memoization


def memoized_cut_rot_aux(p: list, n: int, r: list) -> int:
    """Returns the maximum revenue for a rod of length n."""
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -1
        for i in range(1, n + 1):
            q = max(q, p[i] + memoized_cut_rot_aux(p, n - i, r))
    r[n] = q
    return q


def memoized_cut_rod(p: list, n: int) -> int:
    """Returns the maximum revenue for a rod of length n."""
    r = [-1] * (n + 1)
    return memoized_cut_rot_aux(p, n, r)


# Botton-up approach: iterative with memoization


def memoized_cut_rod_bottom_up(p: list, n: int) -> int:
    """Returns the maximum revenue for a rod of length n."""
    r = [-1 for _ in range(n + 1)]
    r[0] = 0
    for j in range(1, n + 1):
        q = -1
        for i in range(1, j + 1):
            q = max(q, p[i] + r[j - i])
        r[j] = q
    return r[n]


class TestRodCuttingAlgorithms(unittest.TestCase):
    def run_all_tests(self) -> None:
        self.test_cut_rod()
        self.test_top_down_memoized_cut_rod()
        self.test_bottom_up_cut_rod()

    def test_cut_rod(self) -> None:
        p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        self.assertEqual(cut_rod(p, 1), 1)
        self.assertEqual(cut_rod(p, 2), 5)
        self.assertEqual(cut_rod(p, 3), 8)
        self.assertEqual(cut_rod(p, 4), 10)
        self.assertEqual(cut_rod(p, 5), 13)
        self.assertEqual(cut_rod(p, 6), 17)
        self.assertEqual(cut_rod(p, 7), 18)
        self.assertEqual(cut_rod(p, 8), 22)
        self.assertEqual(cut_rod(p, 9), 25)
        self.assertEqual(cut_rod(p, 10), 30)

    def test_top_down_memoized_cut_rod(self) -> None:
        p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        self.assertEqual(memoized_cut_rod(p, 1), 1)
        self.assertEqual(memoized_cut_rod(p, 2), 5)
        self.assertEqual(memoized_cut_rod(p, 3), 8)
        self.assertEqual(memoized_cut_rod(p, 4), 10)
        self.assertEqual(memoized_cut_rod(p, 5), 13)
        self.assertEqual(memoized_cut_rod(p, 6), 17)
        self.assertEqual(memoized_cut_rod(p, 7), 18)
        self.assertEqual(memoized_cut_rod(p, 8), 22)
        self.assertEqual(memoized_cut_rod(p, 9), 25)
        self.assertEqual(memoized_cut_rod(p, 10), 30)

    def test_bottom_up_cut_rod(self) -> None:
        p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        self.assertEqual(memoized_cut_rod_bottom_up(p, 1), 1)
        self.assertEqual(memoized_cut_rod_bottom_up(p, 2), 5)
        self.assertEqual(memoized_cut_rod_bottom_up(p, 3), 8)
        self.assertEqual(memoized_cut_rod_bottom_up(p, 4), 10)
        self.assertEqual(memoized_cut_rod_bottom_up(p, 5), 13)
        self.assertEqual(memoized_cut_rod_bottom_up(p, 6), 17)
        self.assertEqual(memoized_cut_rod_bottom_up(p, 7), 18)
        self.assertEqual(memoized_cut_rod_bottom_up(p, 8), 22)
        self.assertEqual(memoized_cut_rod_bottom_up(p, 9), 25)
        self.assertEqual(memoized_cut_rod_bottom_up(p, 10), 30)


if __name__ == "__main__":
    TestRodCuttingAlgorithms().run_all_tests()
