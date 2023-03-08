from math import fabs


# 1.5.1 а
def Y_precision2(x, e):
    diff = 1
    sum = diff
    i = 1

    precision = 10 ** (-e)

    while fabs(diff) >= precision:
        diff *= -(x / i)
        sum += diff
        i += 1

    return sum


if __name__ == "__main__":
    print("Введите число и точность для 1.5.1 a: ")
    x = [3, 2]# list(map(int, input().split(' ')))
    print(f"1.5.1 а: {Y_precision2(x[0], x[1])}")
