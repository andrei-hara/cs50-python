def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    #the second element of the list
    return float(d.split("$")[1])


def percent_to_float(p):
    #the first element of the list
    return float(p.split("%")[0])/100


main()