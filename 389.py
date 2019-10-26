a = "abcd"
b = "abcde"


for letter in a:
    for letter1 in b:
        if letter != letter1:
            print(letter)