months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    while True:
        date = input("Enter date: ").capitalize()
        try:
            month, day, year = date.split("/")
            if int(month) > 12 or int(day) > 31:
                pass
            else:
                break
        except ValueError:
            try:
                month, day, year = date.split(" ")
                # formatting day
                day = day.split(",")
                # checking if we have comma after day
                if len(day) < 2:
                    pass
                else:
                    day = day[0]
                    # formatting month
                    month = months.index(month) + 1
                    if int(day) > 31:
                        pass
                    else:
                        break
            # exception for the second date.split()
            except ValueError:
                pass

    print(f"{int(year):02}-{int(month):02}-{int(day):02}")


main()
