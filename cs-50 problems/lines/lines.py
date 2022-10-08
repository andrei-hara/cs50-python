import sys

# if argv has 2 elements and the extension of the second element is py
if len(sys.argv) == 2 and sys.argv[1].split(".")[1] == "py":
    python_file = sys.argv[1]
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    sys.exit("Not a python file")

line_counter = 0

try:
    with open(f"{python_file}") as file:
        lines = file.readlines()
        for line in lines:
            # checking blank space or if the line is a comment
            if line.rstrip() != "" and line.lstrip().startswith("#") is False:
                line_counter += 1
# exception for the open function
except FileNotFoundError:
    sys.exit("File does not exist")

print(line_counter)
