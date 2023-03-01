def dig_pow(n, p):
    digits = []
    for digit in str(n):
        digits.append(int(digit))

    sum_pow = 0
    for digit in digits:
        sum_pow += digit ** p
        p += 1

    if sum_pow % n == 0:
        return int(sum_pow / n)

    return -1


if __name__ == "__main__":
    dig_pow(46288, 3)
