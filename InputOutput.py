# In this excise we will be learning how to input and output data
# from the terminal with Python.

# Things to remember: print(), input()
# Symbols: number): steps for complete
#          *word*: Important term


class InputOutput:
    # 1): Declare 2 *global variables* and name them number1
    #     and number2 and set them to 0
    number1 = 0
    number2 = 0

    # Method that will get Input from the user
    def getInput(self):
        self.number1 = int(input("Enter in the first number: "))
        self.number2 = int(input("Enter in the second number: "))

    # Method that will add the two number together
    # 2): add the x and y together and *return* the sum
    def add(self, x, y):
        return x + y

    # Method that will get two numbers from the user and add them
    # together
    def run(self):
        self.getInput()
        return self.add(self.number1, self.number2)


if __name__ == "__main__":
    InputOutput = InputOutput()
    InputOutput.run()
