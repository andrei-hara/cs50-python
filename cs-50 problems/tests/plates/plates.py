def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if check_length(s) and check_first_letters(s) and check_inside_numbers(s) and check_format(s):
        return True
    else:
        return False


def check_length(word):
    # checking the right length
    if  len(word) < 2 or len(word) > 6:
        return False
    else:
        return True


def check_first_letters(word):

    #checking that the first 2 characters are letters
    for character in word[0:2]:
            if character.isalpha() == False:
                return False

    return True


def check_inside_numbers(word):

    #list to get the numbers
    numbers_list = []

    #putting all the numbers in the list
    for number in word:
        if number.isdigit():
            numbers_list += number

    #checking if the first number is 0
    if len(numbers_list) > 0:
        if int(numbers_list[0]) == 0:
            return False

    #taking each character of the string from the 3rd element
    for index in range(2, len(word)-1):
        #checking if the character and the next character are digits
        if word[index].isdigit() and word[index + 1].isalpha():
            return False

    return True


def check_format(word):

    for letter in word:
        #checking if the character is either a letter or number
        if not (letter.isalpha() or letter.isdigit()):
            return False

    return True

if __name__ == "__main__":
    main()