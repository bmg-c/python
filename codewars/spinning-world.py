def spin_words(sentence):
    for word in sentence.split(" "):
        if len(word) > 4:
            sentence = sentence.replace(word, word[::-1])
    return sentence


if __name__ == "__main__":
    spin_words("enviorment why help me please")
