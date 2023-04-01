import math
import random


def jump_search(num, arr):
    n = len(arr)
    step = int(math.sqrt(n))
    pos = 0
    for i in range(0, n, step):
        if arr[i] >= num:
            break
        pos = i

    for i in range(pos, n):
        if arr[i] == num:
            return i

    return -1


def jump_search_2(num, arr):
    n = len(arr)
    step = n
    pos = 0

    while (step > 1):
        for i in range(pos, n, step):
            if arr[i] >= num:
                break
            pos = i
        step = int(math.sqrt(step))

    for i in range(pos, n):
        if arr[i] == num:
            return i

    return -1


def direct_search(num, arr):
    for i in range(0, len(arr)):
        if arr[i] == num:
            return i

    return -1


def create_rand_list():
    randlist = []
    limit = random.randint(10, 20) + 1
    i = 1

    while (i != limit):
        if random.choice([True, False]):
            i += 1
            continue
        randlist.append(i)

    return randlist


if __name__ == "__main__":
    randlist: list[int] = create_rand_list()
    print(randlist)

    num = int(input("Введите число для поиска: "))
    print(f"Поиск прыжками: {jump_search_2(num, randlist)}")

    print(f"Прямой поиск: {direct_search(num, randlist)}")
