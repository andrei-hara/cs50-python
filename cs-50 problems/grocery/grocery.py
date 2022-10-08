def main():
    dict = {}

    while True:
        try:
            item = input("").upper()
            if item in dict:
                dict[item] += 1
            else:
                dict[item] = 1
        except EOFError:
            break

    for value in sorted(dict.keys()):
        print(dict[value], value)


main()
