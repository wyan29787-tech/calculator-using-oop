# Calculator using OOP
class Calculator:
    def __init__(
        self,
        add="add",
        subtract="subtract",
        multiply="multiply",
        divide="divide",
        num1=None,
        num2=None,
        ask=None,
        result=None,
    ):
        self.add = add
        self.subtract = subtract
        self.multiply = multiply
        self.divide = divide
        self.num1 = num1
        self.num2 = num2
        self.ask = ask
        self.result = result

    def calcu(self):
        self.num1 = int(input("Enter a number: "))
        self.num2 = int(input("Enter a number: "))
        self.ask = (
            input(
                "What mathematical operation would you like to perform? (add, subtract, multiply, divide): "
            )
            .strip()
            .lower()
        )
        if self.ask == self.add:
            return self.num1 + self.num2
        elif self.ask == self.subtract:
            return self.num1 - self.num2
        elif self.ask == self.multiply:
            return self.num1 * self.num2
        elif self.ask == self.divide:
            return self.num1 / self.num2
        else:
            print("Invalid Operation!")
        return self.result

    def total(self):
        result = self.calcu()
        print(f"The total is {result}")
        return self.result

    def history(self):
        try:
            with open("calculation_history.txt", "a") as file:
                file.write(f"{self.num1} {self.ask} {self.num2} = {self.result}\n")
            print("Calculation saved to history file.")
        except Exception as e:
            print(f"Could not save to file: {e}")


total = Calculator()
result = total.total()
total.history()
