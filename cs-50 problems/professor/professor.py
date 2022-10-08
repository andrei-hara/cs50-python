import random


def main():
    level = get_level()
    # overall score
    score = 0

    for _ in range(10):
        # generating the two integers
        a, b = generate_integer(level)
        # counter for mistakes
        mistakes = 0

        while True:
            try:
                response = int(input(f"{a} + {b} = "))
                if response == a + b:
                    score += 1
                    break
                else:
                    print("EEE")
                    mistakes += 1
            # exception for the response of the user
            except ValueError:
                print("EEE")
                mistakes += 1
            # if the user makes 3 mistakes, the correct answer is displayed
            if mistakes == 3:
                print(f"{a} + {b} = {a+b}")
                break

    print("Score:", score)


def get_level():
    while True:
        try:
            value = int(input("Level: "))
            if value in [1, 2, 3]:
                return value
            else:
                pass

        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        range_start = pow(10, level-1) - 1
        range_end = pow(10, level) - 1
    else:
        range_start = pow(10, level-1)
        range_end = pow(10, level) - 1

    # generating 2 random numbers from the range of the level
    a = random.randint(range_start, range_end)
    b = random.randint(range_start, range_end)

    return a, b


if __name__ == "__main__":
    main()
