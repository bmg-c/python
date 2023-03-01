# https://www.codewars.com/kata/529adbf7533b761c560004e5/train/python
import sys


def fibonacci(n):
    sys.set_int_max_str_digits(1000000000)
    prev_nums = [0, 1]
    fibonacci_num = 1
    for i in range(2, n + 1):
        fibonacci_num = prev_nums[0] + prev_nums[1]
        prev_nums[0], prev_nums[1] = prev_nums[1], fibonacci_num
    return fibonacci_num


if __name__ == "__main__":
    print(fibonacci(1000000))
