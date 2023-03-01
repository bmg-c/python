def alphabet_position(text):
    alphabet = []
    for char in text:
        alphabet_order = ord(char.upper()) - 64
        if alphabet_order < 1 or alphabet_order > 26:
            continue
        alphabet.append(str(alphabet_order))

    return " ".join(alphabet)


if __name__ == "__main__":
    alphabet_position("zRock and StonE!!")
