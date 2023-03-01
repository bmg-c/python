def expanded_form(num):
    num_str = str(num)
    num_str_length = len(num_str)

    expanded_form_str = []
    for digit in str(num):
        num_str_length -= 1
        part = int(digit) * (10 ** num_str_length)
        if part == 0:
            continue
        expanded_form_str.append(f"{part}")

    return " + ".join(expanded_form_str)


if __name__ == "__main__":
    expanded_form(46088)
