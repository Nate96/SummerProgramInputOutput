import unittest
from InputOutput import InputOutput


class TestInputOutput(unittest.TestCase):
    def setUp(self):
        self.InputOutput = InputOutput()

    def test_globalVariables(self):
        self.assertEqual(0, self.InputOutput.number1)
        self.assertEqual(0, self.InputOutput.number2)

    # This will test getInput method.
    # To run the test click on the little green arrow on the left
    # next to the line number.
    def test_getInput(self):
        self.InputOutput.getInput()

        # Test 1: Enter in 1 for the first number and
        # 2 for the second number.
        self.assertEqual(1, self.InputOutput.number1)
        self.assertEqual(2, self.InputOutput.number2)

        self.InputOutput.getInput()

        # Test 2: enter in 45 for the first number and
        # 100 for the second number
        self.assertEqual(45, self.InputOutput.number1)
        self.assertEqual(100, self.InputOutput.number2)

    # This will test your add method
    def test_add(self):
        self.assertEqual(3, self.InputOutput.add(1, 2))
        self.assertEqual(5, self.InputOutput.add(-5, 10))

    def test_run(self):
        self.assertEqual(10, self.InputOutput.run())