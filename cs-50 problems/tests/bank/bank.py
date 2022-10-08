def main():
    greeting = input("Say a greeting: ").strip()
    print(f"${value(greeting)}")

def value(greeting):
    if greeting.capitalize().split("Hello")[0] == "" and len(greeting.capitalize().split("Hello")) > 1:
        return 0
    elif greeting.capitalize().split("H")[0] == ""  and len(greeting.capitalize().split("H")) > 1:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()