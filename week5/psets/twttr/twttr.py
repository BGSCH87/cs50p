def main():
    word = input("Write me something: ")
    result = shorten(word)
    print(result)


def shorten(word):
    new_word = ""
    for char in word:
        if char.lower() not in ["a", "e", "i", "o", "u"]:
            new_word += char
    return new_word

if __name__ == "__main__":
    main()