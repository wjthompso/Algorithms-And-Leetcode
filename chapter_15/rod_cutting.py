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


# Extended bottom-up approach: Showing the length of the optimal cuts


def extended_bottom_up_cut_rod(p: list, n: int) -> tuple:
    """Returns the maximum revenue for a rod of length n."""
    r = [-1 for _ in range(n + 1)]
    s = [-1 for _ in range(n + 1)]
    r[0] = 0
    for j in range(1, n + 1):
        q = -1
        for i in range(1, j + 1):
            if q < p[i] + r[j - i]:
                q = p[i] + r[j - i]
                s[j] = i
        r[j] = q
    return r, s


def print_cut_rod_solution(p: list, n: int) -> None:
    r, s = extended_bottom_up_cut_rod(p, n)
    while n > 0:
        print(s[n])
        n = n - s[n]


class TestRodCuttingAlgorithms(unittest.TestCase):
    def run_all_tests(self) -> None:
        self.test_cut_rod()
        self.test_top_down_memoized_cut_rod()
        self.test_bottom_up_cut_rod()
        self.test_extended_bottom_up_cut()

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

    def test_extended_bottom_up_cut(self) -> None:
        p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        r, s = extended_bottom_up_cut_rod(p, 1)
        self.assertEqual(r, [0, 1])
        self.assertEqual(s, [-1, 1])
        r, s = extended_bottom_up_cut_rod(p, 2)
        self.assertEqual(r, [0, 1, 5])
        self.assertEqual(s, [-1, 1, 2])
        r, s = extended_bottom_up_cut_rod(p, 3)
        self.assertEqual(r, [0, 1, 5, 8])
        self.assertEqual(s, [-1, 1, 2, 3])
        r, s = extended_bottom_up_cut_rod(p, 4)
        self.assertEqual(r, [0, 1, 5, 8, 10])
        self.assertEqual(s, [-1, 1, 2, 3, 2])
        r, s = extended_bottom_up_cut_rod(p, 5)
        self.assertEqual(r, [0, 1, 5, 8, 10, 13])
        self.assertEqual(s, [-1, 1, 2, 3, 2, 2])
        r, s = extended_bottom_up_cut_rod(p, 6)
        self.assertEqual(r, [0, 1, 5, 8, 10, 13, 17])
        self.assertEqual(s, [-1, 1, 2, 3, 2, 2, 6])
        r, s = extended_bottom_up_cut_rod(p, 7)
        self.assertEqual(r, [0, 1, 5, 8, 10, 13, 17, 18])
        self.assertEqual(s, [-1, 1, 2, 3, 2, 2, 6, 1])


if __name__ == "__main__":
    TestRodCuttingAlgorithms().run_all_tests()

    r, s = extended_bottom_up_cut_rod([0, 1, 5, 8, 10, 13, 17, 18, 22, 25, 30], 9)

    print_cut_rod_solution([0, 1, 5, 8, 10, 13, 17, 18, 22, 25, 30, 0, 0, 0, 0, 0], 14)
