from math import fabs


# 1.4.7 б
def Y_sum(n):
    sum = 0

    for i in range(1, n + 1):
        sum += i ** (-i)  # (1 / n) ** i

    return sum


# 1.5.1 б
def Y_precision(x, e):
    diff = x
    sum = diff
    i = 3

    while fabs(diff) >= e:
        diff *= -((x ** 2) / ((i - 1) * i))
        sum += diff
        i += 2

    return sum


# 1.5.1 а
def Y_precision2(x, e):
    diff = 1
    sum = diff
    i = 1  # Для факториала

    while fabs(diff) >= e:
        diff *= -(x / i)  # Каждую итерацию находит след. элемент используя
        # разность между каждыми
        sum += diff  # Добавляет элемент в сумму
        i += 1

    return sum


# 1.5.1 д
def Y_precision3(x, e):
    diff = 1
    sum = diff
    i = 2

    while fabs(diff) >= e:
        diff *= (x ** 2) / (i * (i - 1))
        sum += diff
        i += 2

    return sum


# 1.5.1 ж
def Y_precision4(x, e):
    diff = x
    sum = diff
    i = 1

    while fabs(diff) >= e:
        diff *= -(i / (i + 1)) * ((x ** 2) / (i + 2)) * (i - 2)
        sum += diff
        i += 2

    return sum


if __name__ == "__main__":
    # x = [3, 0.01]

    print("Введите число для 1.4.7 б: ")
    x = int(input())
    print(f"1.4.7 б: {Y_sum(x)}")

    print("\nВведите число и точность для 1.5.1 б: ")
    x = list(map(float, input().split(' ')))
    print(f"1.5.1 б: {Y_precision(x[0], x[1])}")

    print("\nВведите число и точность для 1.5.1 a: ")
    x = list(map(float, input().split(' ')))
    print(f"1.5.1 a: {Y_precision2(x[0], x[1])}")

    print("\nВведите число и точность для 1.5.1 д: ")
    x = list(map(float, input().split(' ')))
    print(f"1.5.1 д: {Y_precision3(x[0], x[1])}")

    print("\nВведите число и точность для 1.5.1 ж: ")
    x = list(map(float, input().split(' ')))
    print(f"1.5.1 ж: {Y_precision4(x[0], x[1])}")
