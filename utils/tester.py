from unittest import TestCase


class UnitTester(TestCase):
    def run_all_tests(self):
        """Run all defined tests in the class."""
        # Write code here that finds all of the tests defined in the class that
        # are not private (i.e. do not start with an underscore) and are not the
        # current method and runs them.
        method_names = [
            method for method in dir(self) if callable(getattr(self, method))
        ]

        test_methods = [
            method
            for method in method_names
            if method.startswith("test_") and method != "run_all_tests"
        ]

        # Run each test method
        for method in test_methods:
            getattr(self, method)()
