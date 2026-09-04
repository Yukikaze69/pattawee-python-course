print("\n=== ITERATING THROUGH STRING ===")
count = 0
text = input("insert your text: ")
char = input("character to find: ")
for letter in text:
    if letter == char:
        count += 1
print(f"{count} letters {char} found in '{text}'")





password = input("Enter password:")
lenght = len(password)
word = password.spilt('@')
if len(word) > 1 and password.count('@') == 1:
    left = word[0].isalnum()
    right = word[1].isalnum()
else
    left = False:
    right = False:


if lenght >= 8 and len(word) == 2 and left and right:
    print("your password is strong")
else
    print("your password is not strong")    

