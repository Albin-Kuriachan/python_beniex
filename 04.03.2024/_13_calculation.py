""".Implement a program that simulates a basic calculator, allowing users to
perform arithmetic operations (addition, subtraction, multiplication,division) on two numbers."""


class Calculator:

    def addition(self, num1, num2):
        return num1 + num2

    def subtraction(self, num1, num2):
        return num1 - num2

    def multiplication(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2

    def calculate(self):

        print("Select From the List")
        print("A for Addition")
        print("B for Subtraction")
        print("C for Multiplication")
        print("D for Division")

        choice = input("Enter operation number (A/B/C/D): ").upper()

        if choice not in ('A', 'B', 'C', 'D'):
            print(f"{choice} is not a valid operation.")
            return

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 'A':
            print("Result:", self.addition(num1, num2))
        elif choice == 'B':
            print("Result:", self.subtraction(num1, num2))
        elif choice == 'C':
            print("Result:", self.multiplication(num1, num2))
        elif choice == 'D':
            print("Result:", self.division(num1, num2))


obj = Calculator()
obj.calculate()
