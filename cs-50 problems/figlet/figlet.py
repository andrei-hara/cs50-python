from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

if len(sys.argv) == 1:
    response = input("Input: ")
    # random font
    f = random.choice(figlet.getFonts())
    # setting up the font
    figlet.setFont(font=f)
    # printing the output
    print(figlet.renderText(response))

elif len(sys.argv) == 3:
    if (sys.argv[1] in ["-f", "--font"]) and (sys.argv[2] in figlet.getFonts()):
        # getting the user input
        response = input("Input: ")
        # setting the font via argv
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(response))
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")
