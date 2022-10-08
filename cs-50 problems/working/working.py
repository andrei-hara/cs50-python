import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^(\d{1,2}(?:\:\d{2})?)\s{1}(AM|PM)\s{1}to\s{1}(\d{1,2}(?:\:\d{2})?)\s{1}(AM|PM)$", s):
        # taking the hours and abreviations
        first = matches.group(1)
        first_abv = matches.group(2)
        last = matches.group(3)
        last_abv = matches.group(4)

        # try to split if the format is ##:##
        try:
            hours_first, minutes_first = first.split(":")
            hours_last, minutes_last = last.split(":")

        except ValueError:
            hours_first, minutes_first = first, "00"
            hours_last, minutes_last = last, "00"

        # checking if the hours and minutes are in the right margins
        if (int(hours_first) > 12 or int(hours_first) < 1) and first_abv == "AM":
            raise ValueError
        if (int(hours_first) > 12 or int(hours_first) < 1)  and first_abv == "PM":
            raise ValueError
        if (int(hours_last) > 12 or int(hours_last) < 1) and last_abv == "AM":
            raise ValueError
        if (int(hours_last) > 12 or int(hours_last) < 1)  and last_abv == "PM":
            raise ValueError
        if int(minutes_first) >= 60 or int(minutes_last) >= 60:
            raise ValueError

        # converting format
        if first_abv == "PM" and hours_first == "12":
            pass
        if first_abv == "PM" and hours_first != "12":
            hours_first = int(hours_first) + 12

        if last_abv == "PM" and hours_last == "12":
            pass
        if last_abv == "PM" and hours_last != "12":
            hours_last = int(hours_last) + 12

        if first_abv == "AM" and hours_first == "12":
            hours_first = 0
        if last_abv == "AM" and hours_last == "12":
            hours_last = 0

        return f"{int(hours_first):02}:{minutes_first} to {int(hours_last):02}:{minutes_last}"

    # if the format is not right
    else:
        raise ValueError


if __name__ == "__main__":
    main()