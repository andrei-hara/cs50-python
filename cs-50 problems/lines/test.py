vowels = ['A', 'E', 'I', 'O', 'U']

text = input("Insert text: ")
format_text = ""

for character in text:
    if character.upper() not in vowels:
        format_text += character

# line to test the comments
print(format_text)