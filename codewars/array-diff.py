def array_diff(a, b):
    diff = []
    for num in a:
        if num not in b:
            diff.append(num)

    return diff


if __name__ == "__main__":
    array_diff([2, 5, 5, 5, 10], [5])
