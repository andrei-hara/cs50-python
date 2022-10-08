from validator_collection import validators


def main():
    email = input("What's your email address? ")
    if check(email):
        print("Valid")
    else:
        print("Invalid")


def check(s):
    try:
        email_address = validators.email(s)
        return True
    except:
        return False


if __name__ == "__main__":
    main()
