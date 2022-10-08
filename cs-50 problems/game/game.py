import random
import sys

while True:
    try:
        number = int(input("Level: "))
        if number > 0:
            random_number = random.randint(1, number)
            while True:
                guess = int(input("Guess: "))
                if guess > random_number:
                    print("Too large!")
                elif guess < random_number:
                    print("Too small!")
                else:
                    # Exiting the program
                    sys.exit("Just right!")
        else:
            pass

    # Exception for the value number
    except ValueError:
        pass
