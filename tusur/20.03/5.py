class Calculator:
    def __init__(self) -> None:
        self.operations = {
            "+": self._sum,
            "-": self._sub,
            "/": self._div,
            "*": self._mul,
        }

    def calculate(self, number1: float, number2: float, operand: str) -> float:
        func = self.operations.get(operand)

        if func is None:
            raise NotImplementedError()

        return func(number1, number2)

    def _sum(self, number1: float, number2: float) -> float:
        return number1 + number2

    def _sub(self, number1: float, number2: float) -> float:
        return number1 - number2

    def _div(self, number1: float, number2: float) -> float:
        return number1 / number2

    def _mul(self, number1: float, number2: float) -> float:
        return number1 * number2

    def __str__(self) -> str:
        return "Калькулятор"


def get_expression() -> tuple[float, str, float]:
    while True:
        try:
            expression: list[str] = input("Введите выражение: ").split()

            return float(expression[0]), expression[1], float(expression[2])
        except ValueError:
            print("Введите выражение еще раз!")


def return_value(value) -> None:
    print(value)


def main() -> None:
    # В Python все является объектом => мы можем сделать
    # a = Calculator; calculator = a()

    calculator = Calculator()
    num1, operand, num2 = get_expression()

    value = calculator.calculate(num1, num2, operand)
    return_value(value)

    print(calculator)


if __name__ == "__main__":
    main()
