due = 50
coin_list = [5, 10, 25, 50]

while True:
    print(f"Amount due: {due}")
    coin = int(input("Insert coin: "))

    #Verifying that the coin is valid
    if coin in coin_list:
        due -= coin

    if due <= 0:
        print("Change owed:", abs(due))
        break


