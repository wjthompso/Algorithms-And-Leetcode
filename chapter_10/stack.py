from typing import List, Union, Any
from unittest import TestCase


class Stack:
    def __init__(self, size: int):
        self.stack: List[Union[str, int]] = [None] * size
        self.top = -1
        self.size = size

    def stack_empty(self) -> bool:
        if self.top == -1:
            return True
        return False

    def stack_full(self) -> bool:
        if self.top == self.size - 1:
            return True
        return False

    def push(self, x: int) -> None:
        if self.stack_full():
            raise Exception("Stack overflow")
        self.top += 1
        self.stack[self.top] = x

    def pop(self) -> int:
        if self.stack_empty():
            raise Exception("Stack underflow")
        self.top -= 1
        return self.stack[self.top + 1]


class UnitTester(TestCase):
    def run_all_tests(self):
        """Run all defined tests in the class."""
        self.test_1()
        self.test_2()

    def test_1(self):
        """Test the stack code."""
        stack = Stack(5)
        self.assertTrue(stack.stack_empty())
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertFalse(stack.stack_empty())
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertTrue(stack.stack_empty())
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        self.assertTrue(stack.stack_full())
        with self.assertRaises(Exception):
            stack.push(6)
        self.assertEqual(stack.pop(), 5)
        self.assertEqual(stack.pop(), 4)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertTrue(stack.stack_empty())
        with self.assertRaises(Exception):
            stack.pop()

    def test_2(self):
        stack: Stack = Stack(5)
        assert stack.stack_empty() == True
        stack.push(1)
        assert stack.pop() == 1


if __name__ == "__main__":
    tester = UnitTester()
    tester.run_all_tests()
