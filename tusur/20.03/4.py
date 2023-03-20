
if __name__ == "__main__":
    randomlist = random.sample(range(1, 11), 10)
    print(randomlist)
    print()

    comb_sort(randomlist)
    print(randomlist)
    print("\n")

    random2dlist = list()
    for i in range(0, 10):
        random2dlist.append(random.sample(range(1, 91), 10))
    print(random2dlist)
    print()

    comb_sort_2d(random2dlist)
    for i in range(0, len(random2dlist)):
        print(random2dlist[i])
