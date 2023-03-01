def max_sequence(arr):
    if len(arr) == 0:
        return 0

    sum = 0
    neg_num_count = 0
    for i in range(len(arr)):
        temp_sum = 0
        if arr[i] < 0:
            neg_num_count += 1
        for j in range(len(arr) - i):
            temp_sum += arr[i + j]
            if temp_sum > sum:
                sum = temp_sum
    if neg_num_count == len(arr):
        return 0

    return sum


if __name__ == "__main__":