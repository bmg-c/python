import random


def comb_sort(arr):
    n = len(arr)
    step = n - 1

    while (step > 0):
        i = 0
        j = step

        while (j < n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            j += 1
            i += 1
            # print(arr)

        step -= 1


def comb_sort_2d(arr):
    n = len(arr)
    n_row = len(arr[0])
    step = n * n_row - 1

    while (step > 0):
        i = 0
        j = step

        while (j < n * n_row):
            if arr[i // n_row][i % n_row] > arr[j // n_row][j % n_row]:
                arr[i // n_row][i % n_row], arr[j // n_row][j % n_row] = arr[j // n_row][j % n_row], arr[i // n_row][i % n_row]
            j += 1
            i += 1

        step -= 1


if __name__ == "__main__":
    randomlist = random.sample(range(1, 11), 10)
    print(randomlist)
    print()

    comb_sort(randomlist)
    print(randomlist)
    print("\n")

    random2dlist = list()
    for i in range(0, 10):
        random2dlist.append(random.sample(random.sample(range(1, 91), 10), 10))
    print(random2dlist)
    print()

    comb_sort_2d(random2dlist)
    for i in range(0, len(random2dlist)):
        print(random2dlist[i])
