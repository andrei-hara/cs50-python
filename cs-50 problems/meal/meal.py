def main():
    user_input = input("What time is it? ")

    if 7 <= convert(user_input) <= 8:
        print("breakfast time")
    elif 12 <= convert(user_input) <= 13:
        print("lunch time")
    elif 18 <= convert(user_input) <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")

    return float(hours) + float(minutes) / 60


if __name__ == "__main__":
    main()