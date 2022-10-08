import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        address = matches.groups()
        for i in address:
            if int(i) <= 255:
                pass
            else:
                return False
        return True

    return False


if __name__ == "__main__":
    main()
