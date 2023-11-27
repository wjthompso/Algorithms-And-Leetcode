from typing import List, Union, Any
from unittest import TestCase


class Queue:
    def __init__(self, n: int):
        self.queue: List[Union[str, int]] = [None] * n
        self.head = 0
        self.tail = 0
        self.length = n

    def queue_empty(self) -> int:
        if self.head == self.tail:
            return True
        return False

    def queue_full(self) -> int:
        if (self.tail + 1 == self.head) or (
            (self.tail == self.length - 1) and (self.head == 0)
        ):
            return True
        return False

    def enqueue(self, x: int) -> None:
        if self.queue_full():
            raise Exception("Queue overflow")

        self.queue[self.tail] = x
        if self.tail == self.length - 1:
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self) -> int:
        if self.queue_empty():
            raise Exception("Queue underflow")

        x = self.queue[self.head]
        if self.head == self.length - 1:
            self.head = 1
        else:
            self.head += 1
        return x


# Test the queue code


class UnitTester(TestCase):
    def run_all_tests(self):
        """Run all defined tests in the class."""
        # Write code here that finds all of the tests defined in the class that
        # are not private (i.e. do not start with an underscore) and are not the
        # current method and runs them.
        # method_names = [
        #     method for method in dir(self) if callable(getattr(self, method))
        # ]

        # test_methods = [
        #     method
        #     for method in method_names
        #     if method.startswith("test_") and method != "run_all_tests"
        # ]

        # # Run each test method
        # for method in test_methods:
        #     getattr(self, method)()
        self.test_queue_1()
        self.test_queue_2()
        self.test_queue_3()
        self.test_queue_4()

    def test_queue_1(self):
        queue = Queue(3)
        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.dequeue() == 1
        assert queue.dequeue() == 2

    def test_queue_2(self):
        queue = Queue(5)
        queue.enqueue(4)
        queue.enqueue(1)
        queue.enqueue(3)
        queue.enqueue(16)
        assert queue.dequeue() == 4
        assert queue.dequeue() == 1
        assert queue.dequeue() == 3
        assert queue.dequeue() == 16

    def test_queue_3(self):
        queue = Queue(3)
        queue.enqueue(1)
        queue.enqueue(2)
        with self.assertRaises(Exception) as context:
            queue.enqueue(4)

        # Check if the exception message is "Queue overflow!"
        self.assertEqual(str(context.exception), "Queue overflow")

    def test_queue_4(self):
        queue = Queue(3)
        with self.assertRaises(Exception) as context:
            queue.dequeue()
        self.assertEqual(str(context.exception), "Queue underflow")


if __name__ == "__main__":
    UnitTester().run_all_tests()
