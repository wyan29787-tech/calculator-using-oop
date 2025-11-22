# Calculator using OOP
class Calculator:
    def __init__(self):
        self.num1 = None
        self.num2 = None
        self.operation = None
        self.result = None

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        return num1 / num2

    def calculate(self, num1, num2, operation):
        self.num1 = num1
        self.num2 = num2
        self.operation = operation.strip().lower()

        if self.operation == "add":
            self.result = self.add(num1, num2)
        elif self.operation == "subtract":
            self.result = self.subtract(num1, num2)
        elif self.operation == "multiply":
            self.result = self.multiply(num1, num2)
        elif self.operation == "divide":
            self.result = self.divide(num1, num2)
        else:
            raise ValueError(f"Invalid operation: {operation}")

        return self.result

    def interface(self):
        try:
            self.num1 = int(input("Enter a number: "))
            self.num2 = int(input("Enter a number: "))
            self.operation = (
                input(
                    "What mathematical operation would you like to perform? (add, subtract, multiply, divide): "
                )
                .strip()
                .lower()
            )

            self.result = self.calculate(self.num1, self.num2, self.operation)
            print(f"The total is {self.result}")
            self.save_to_history()
            return self.result
        except ValueError as e:
            print(f"Error: {e}")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def save_to_history(self):
        """Save calculation to history file"""
        try:
            with open("calculation_history.txt", "a") as file:
                file.write(
                    f"{self.num1} {self.operation} {self.num2} = {self.result}\n"
                )
            print("Calculation saved to history file.")
        except Exception as e:
            print(f"Could not save to file: {e}")


if __name__ == "__main__":
    calc = Calculator()
    calc.interface()
