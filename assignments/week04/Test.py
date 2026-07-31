Name = (input("What is you name?: "))
letter = list(Name)
count = 0
for letter in Name:
    if letter == 'a'or letter == 'A':
        count = count + 1
    if letter == 'e'or letter == 'E':
            count = count + 1    
    if letter == 'i'or letter == 'I':
        count = count + 1
    if letter == 'o'or letter == 'O':
            count = count + 1    
    if letter == 'u'or letter == 'U':
            count = count + 1   
    print(f"ตัวอักษร: {letter}")

print("your text have",count,"vowels" )