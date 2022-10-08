import sys

def main():

    user_input = input(("Fraction: "))
    percentage = convert(user_input)
    print(gauge(percentage))


def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            value = int(x) / int(y)
            if 0 <= value < 1:
                return round(value*100)
            else:
                fraction = input("Fraction: ")

        except(ZeroDivisionError, ValueError):
            raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()