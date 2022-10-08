def main():

    text = input("Insert text: ")
    print(shorten(text))


def shorten(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    format_text = ""

    for character in word:
        if (character.upper() not in vowels):
            format_text += character

    return format_text


if __name__ == "__main__":
    main()