from datetime import date
import re
import inflect
import sys


def main():
    # initializing inflect
    p = inflect.engine()
    user_input = input("Date of birth: ")
    if validate_format(user_input):
        minutes = convert_minutes(user_input)
        print(p.number_to_words(minutes).capitalize().replace("and ", ""), "minutes")


def validate_format(user_date):
    if match := re.search(r"^(\d{4})-(\d{2})-(\d{2})$", user_date):
        years = match.group(1)
        months = match.group(2)
        days = match.group(3)
        try:
            date(int(years), int(months), int(days))
            return True
        except ValueError:
            sys.exit("Invalid date")

    else:
        sys.exit("Invalid date")


def convert_minutes(born_date):
    # born date
    b_years, b_months, b_days = born_date.split("-")
    born_time = date(int(b_years), int(b_months), int(b_days))
    # current date
    current_time = date.today()

    timedelta = current_time - born_time
    # transforming days into minutes
    if timedelta.days >= 0:
        return timedelta.days * 24 * 60
    else:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
