def main():
    weight = input("Enter a mass in kilograms: ")
    speed = 300000000
    energy = int(weight) * pow(speed, 2)

    print(energy)

main()