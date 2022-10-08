import sys
import csv
from tabulate import tabulate


def main():
    file_name = take_argument()
    menu_items = csv_reader(file_name)

    # first element is the table without the header, the second is the header, the third is the table format
    print(tabulate(menu_items[1:], menu_items[0], tablefmt="grid"))


def take_argument():
    # if argv has 2 elements and the extension of the second element is csv
    if len(sys.argv) == 2 and sys.argv[1].split(".")[1] == "csv":
        return sys.argv[1]
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Not a python file")


def csv_reader(name):
    menu_items = []

    try:
        with open(f"{name}") as file:
            # reading the csv file with the csv reader
            reader = csv.reader(file)
            # appending the csv lines to the list
            for pizza, small, large in reader:
                menu_items.append([pizza, small, large])

            return menu_items
    # exception for the open function
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
