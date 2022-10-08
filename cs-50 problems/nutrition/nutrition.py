fruits = {"apple" : "130", "avocado" : "50", "banana" : "110",
          "cantaloupe" : "50", "grapefruit" : "60", "grapes" : "90",
          "honeydew melon" : "50", "kiwifruit" : "90", "lemon" : "15",
          "sweet cherries" : "100", "pear" : "100"}

def main():
    fruit = input("Enter fruit: ").lower()
    if fruit in fruits:
        print(fruits[fruit])

main()