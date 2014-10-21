import unittest
import sys
from io import StringIO

from app import FizzBuzz

class TestSuite(unittest.TestCase):

    def test_one(self):
        app = FizzBuzz()
        self.assertFalse(app.calc(1) != 1)

    def test_run(self):
        output = StringIO()

        app = FizzBuzz()
        app.run(100, output)

        self.assertFalse(len(output.getvalue().splitlines()) != 99)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
