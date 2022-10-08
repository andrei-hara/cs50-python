def main():
    fuel = get_fuel()
    print(fuel)


def get_fuel():
    # try:
    while True:
        user_input = input(("Fraction: "))

        try:
            x, y = user_input.split("/")
            value = int(x) / int(y)
            if 0 <= value < 0.25:
                return "E"
            elif 1 >= value > 0.75:
                return "F"
            elif value > 1:
                pass
            else:
                return str(int(round(value*100, 0))) + "%"
        except (ZeroDivisionError, ValueError):
            pass


main()
