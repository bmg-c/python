class FractionalNum:
    def _find_gcd(self):
        a = self.numerator
        b = self.denominator

        while (b != 0):
            a, b = b, a % b

        return a

    def _reduce_fraction(self):
        gcd = self._find_gcd()

        self.numerator /= gcd
        self.denominator /= gcd

    def __init__(self, numerator: int, denominator: int):
        self.numerator: int = numerator
        self.denominator: int = denominator

        self._reduce_fraction()

    def __str__(self):
        if abs(self.numerator) < abs(self.denominator):
            return f"{int(self.numerator)} / {int(self.denominator)}"

        numerator: int = abs(self.numerator)
        denominator: int = abs(self.denominator)

        if self.numerator < 0 or self.denominator < 0:
            integer: int = -(numerator // denominator)
        else:
            integer: int = numerator // denominator

        numerator = numerator % denominator

        if numerator == 0:
            return f"{int(integer)}"

        return f"{int(integer)} ({int(numerator)} / {int(denominator)})"

    def __add__(self, other):
        numerator = self.numerator * other.denominator + \
            other.numerator * self.denominator
        denominator = self.denominator * other.denominator

        return FractionalNum(int(numerator), int(denominator))

    def __iadd__(self, other):
        numerator = self.numerator * other.denominator + \
            other.numerator * self.denominator
        denominator = self.denominator * other.denominator

        self.numerator = int(numerator)
        self.denominator = int(denominator)

        self._reduce_fraction()

        return self

    def __sub__(self, other):
        numerator = self.numerator * other.denominator - \
            other.numerator * self.denominator
        denominator = self.denominator * other.denominator

        return FractionalNum(int(numerator), int(denominator))

    def __isub__(self, other):
        numerator = self.numerator * other.denominator - \
            other.numerator * self.denominator
        denominator = self.denominator * other.denominator

        self.numerator = int(numerator)
        self.denominator = int(denominator)

        self._reduce_fraction()

        return self

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator

        return FractionalNum(int(numerator), int(denominator))

    def __imul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator

        self.numerator = int(numerator)
        self.denominator = int(denominator)

        self._reduce_fraction()

        return self

    def __truediv__(self, other):
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator

        return FractionalNum(int(numerator), int(denominator))

    def __itruediv__(self, other):
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator

        self.numerator = int(numerator)
        self.denominator = int(denominator)

        self._reduce_fraction()

        return self
