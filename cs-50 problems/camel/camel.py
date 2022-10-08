user_input = input("Enter name:")
modified_input = ""

for character in range(len(user_input)):
      if(user_input[character] != user_input[character].upper()):
            modified_input += user_input[character]
      else:
            modified_input +=  "_" + user_input[character].lower()

print(modified_input)