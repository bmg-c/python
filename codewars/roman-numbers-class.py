class RomanNumerals:

    def to_roman(val):
        str = []
        digits = []
        digits.append(int(val / 1000))
        digits.append(int((val - digits[0] * 1000) / 100))
        digits.append(int((val - digits[0] * 1000 - digits[1] * 100) / 10))
        digits.append(val - digits[0] * 1000 -
                      digits[1] * 100 - digits[2] * 10)
        for i in range(digits[0]):
            str.append("M")

        if digits[1] < 4:
            for i in range(digits[1]):
                str.append("C")
        elif digits[1] == 4:
            str.append("CD")
        elif digits[1] < 9:
            str.append("D")
            digits[1] -= 5
            for i in range(digits[1]):
                str.append("C")
        elif digits[1] == 9:
            str.append("CM")

        if digits[2] < 4:
            for i in range(digits[2]):
                str.append("X")
        elif digits[2] == 4:
            str.append("XL")
        elif digits[2] < 9:
            str.append("L")
            digits[2] -= 5
            for i in range(digits[2]):
                str.append("X")
        elif digits[2] == 9:
            str.append("XC")

        if digits[3] < 4:
            for i in range(digits[3]):
                str.append("I")
        elif digits[3] == 4:
            str.append("IV")
        elif digits[3] < 9:
            str.append("V")
            digits[3] -= 5
            for i in range(digits[3]):
                str.append("I")
        elif digits[3] == 9:
            str.append("IX")

        return "".join(str)

    def from_roman(roman_num):
        symbols = list(roman_num)
        number = 0
        step = 0

        while step < len(symbols) and symbols[step] == "M":
            number += 1000
            step += 1

        if step < len(symbols) - 1 and symbols[step] == "C" and symbols[step + 1] == "M":
            number += 900
            step += 2
        if step < len(symbols) - 1 and symbols[step] == "C" and symbols[step + 1] == "D":
            number += 400
            step += 2
        if step < len(symbols) and symbols[step] == "D":
            number += 500
            step += 1
        while step < len(symbols) and symbols[step] == "C":
            number += 100
            step += 1

        if step < len(symbols) - 1 and symbols[step] == "X" and symbols[step + 1] == "C":
            number += 90
            step += 2
        if step < len(symbols) - 1 and symbols[step] == "X" and symbols[step + 1] == "L":
            number += 40
            step += 2
        if step < len(symbols) and symbols[step] == "L":
            number += 50
            step += 1
        while step < len(symbols) and symbols[step] == "X":
            number += 10
            step += 1

        if step < len(symbols) - 1 and symbols[step] == "I" and symbols[step + 1] == "X":
            number += 9
            step += 2
        if step < len(symbols) - 1 and symbols[step] == "I" and symbols[step + 1] == "V":
            number += 4
            step += 2
        if step < len(symbols) and symbols[step] == "V":
            number += 5
            step += 1
        while step < len(symbols) and symbols[step] == "I":
            number += 1
            step += 1

        return number


if __name__ == "__main__":
    RomanNumerals.to_roman(1990)
    RomanNumerals.from_roman('MCMXC')
