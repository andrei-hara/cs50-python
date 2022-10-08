def convert(string):
    print(string.replace(":)", "🙂").replace(":(", "🙁"))


def main():
    sentence = input("Enter your text: ")
    convert(sentence)


main()