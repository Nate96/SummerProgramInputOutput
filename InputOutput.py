class InputOutput:
    number1: int = 0
    number2: int = 0

    def getInput(self):
        self.number1 = int(input("Enter in the first number: "))
        self.number2 = int(input("Enter in the second number: "))

    def add(self, x, y):
        return x + y

    def run(self):
        self.getInput()
        return self.add(self.number1, self.number2)

if __name__ == "__main__":
    InputOutput = InputOutput()
    InputOutput.run()
