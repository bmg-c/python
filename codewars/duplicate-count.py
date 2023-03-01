def duplicate_count(text):
    duplicate_amount = 0
    index = 0
    counted_chars = [" "]
    for char in text.upper():
        index += 1
        if char in counted_chars:
            continue
        counted_chars.append(char)

        for next_char in text.upper()[index:]:
            if char == next_char:
                duplicate_amount += 1
                break

    return duplicate_amount


if __name__ == "__main__":
    duplicate_count("abcdeaB")
