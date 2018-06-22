import unittest
from InputOutput import InputOutput

class TestInputOuput(unittest.TestCase):
    def setUp(self):
        self.InputOutput = InputOutput()

    def test_getInput(self):
        self.InputOutput.getInput()

        self.assertEqual(1, self.InputOutput.number1)
        self.assertEqual(2, self.InputOutput.number2)

        self.InputOutput.getInput()

        self.assertEqual(45, self.InputOutput.number1)
        self.assertEqual(100, self.InputOutput.number2)

    def test_add(self):
        self.assertEqual(3, self.InputOutput.add(1, 2))
        self.assertEqual(5, self.InputOutput.add(-5, 10))

    def test_run(self):
        self.assertEqual(10, self.InputOutput.run())