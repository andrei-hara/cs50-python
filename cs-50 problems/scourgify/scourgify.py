import sys
import csv


def main():
    # taking the input csv and output csv
    input, output = take_arguments()

    # reading the csv file
    students_list = read_csv(input)

    # formatting the name of students
    formatted_students = convert_csv(students_list)

    # writing the formatted stundents in another file
    write_csv(formatted_students, output)


def take_arguments():
    # if argv has 3 elements and the extension of the second and third element is csv
    if len(sys.argv) == 3 and ".csv" in (sys.argv[1] and sys.argv[2]):
        return sys.argv[1], sys.argv[2]
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Not a csv file")


def read_csv(csv_input):
    student_list = []
    try:
        # taking the input from the first csv file
        with open(f"{csv_input}") as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = {"name" : row["name"], "house" : row["house"]}
                student_list.append(student)

        return student_list

    except FileNotFoundError:
        sys.exit("File does not exist")


def convert_csv(students):
    new_students = []
    for student in students:
        # splitting the dictionary into 3 fields
        first_name, last_name = student["name"].split(", ")
        house = student["house"]
        # replacing the value of the full name with the second name
        new_students.append({"first" : first_name, "last" : last_name, "house" : house})

    return new_students


def write_csv(students, output):

    with open(f"{output}", "w") as file:
        file.write(f"first,last,house\n")
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        for student in students:
            # print(student)
            writer.writerow({"first" : student["last"], "last": student["first"], "house" : student["house"]})


if __name__ == "__main__":
    main()

