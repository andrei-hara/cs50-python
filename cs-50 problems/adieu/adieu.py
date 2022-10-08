import inflect

names = []
p = inflect.engine()

while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        print("Adieu, adieu, to", p.join(names))
        break
