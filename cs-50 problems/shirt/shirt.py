import sys
from PIL import Image, ImageOps


def main():
    input, output = take_user_input()
    image_converter(input, output)


def take_user_input():
    if len(sys.argv) == 3 and (
        sys.argv[1].split(".")[1]
        and (sys.argv[2].split(".")[1]) in ["jpg", "png", "jpeg"]
    ):
        # checking if the arguments have the same extension
        if sys.argv[1].split(".")[1] == sys.argv[2].split(".")[1]:
            return sys.argv[1], sys.argv[2]
        else:
            sys.exit("Input and output have different extensions")

    elif len(sys.argv) < 3:
        sys.exit("Too few arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many arguments")
    else:
        sys.exit("Invalid input")


def image_converter(before, after):
    try:
        # open img
        photo = Image.open(before)
        # open shirt
        shirt = Image.open("shirt.png")
        size = shirt.size
        # resize the person - first arg the photo that we want to resize, the second the size
        person = ImageOps.fit(photo, size)
        # pasting the shirt on the person
        person.paste(shirt, shirt)
        # saving the image in the file with the name of the argline output
        person.save(after)

    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
