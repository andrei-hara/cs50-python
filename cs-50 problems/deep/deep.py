answer = input("What's the answer to the great question of life? ").lower().strip()

match(answer):
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")