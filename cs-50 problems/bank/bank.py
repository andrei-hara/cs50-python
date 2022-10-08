greeting = input("Say a greeting: ").lower().strip()

if greeting.split("hello")[0] == "":
    print("$0")
elif greeting.split("h")[0] == "":
    print("$20")
else:
    print("$100")