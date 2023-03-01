def disemvowel(string_):
    list_new = []
    for char in string_:
        if char.upper() not in {"A", "E", "O", "U", "I"}:
            list_new.append(char)
    return ''.join(list_new)


if __name__ == "__main__":
    disemvowel("Rock and StonE!!")
