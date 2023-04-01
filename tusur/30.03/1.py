import math
import random


def comb_rep_amount(arr, k):
    n = len(arr)
    if (n <= 0 or k <= 0):
        return 0

    return int(math.factorial(k + n - 1) / (math.factorial(n - 1) *
                                            math.factorial(k)))


if __name__ == "__main__":
    # arr: list[int] = []
    # for i in range(0, 5):
    #     arr.append(random.randint(1, 30))
    # print(arr)

    dimensions = list(map(int, input("Введите n и k: ").split(' ')))
    randomlist = random.sample(range(1, dimensions[0] + 1), dimensions[0])
    randomlist = list(range(1, dimensions[0] + 1))
    print(randomlist)

    print("Количество сочетаний с повторениями: "
          + f"{comb_rep_amount(randomlist, dimensions[1])}")
