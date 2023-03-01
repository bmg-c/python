def solution(n):
    str = []
    digits = []
    digits.append(int(n / 1000))
    digits.append(int((n - digits[0] * 1000) / 100))
    digits.append(int((n - digits[0] * 1000 - digits[1] * 100) / 10))
    digits.append(n - digits[0] * 1000 - digits[1] * 100 - digits[2] * 10)
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


if __name__ == "__main__":
    solution(2989)
