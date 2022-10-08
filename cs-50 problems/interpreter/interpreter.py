x, y, z = input("Enter expression: ").split(" ")

if y == "+":
     print(round((float(x) + float(z)), 1))
elif y == "-":
     print(round((float(x) - float(z)), 1))
elif y == "*":
     print(round((float(x) * float(z)), 1))
elif y == "/" and z != 0:
     print(round((float(x) / float(z)), 1))




