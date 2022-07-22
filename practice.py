#!/usr/bin/env python3

'''
a = 3
b = 5
print("a is {} and b is {}".format(a,b))

num = 3456876
list = str(num)
print(type(num))
print(type(list))

'''

text = input("phrase to encrypt: ")
shift = int(input("shift amount? "))
cipher = ""
for i in range(len(text)):
    char = text[i]
    if (char.isupper()):
        cipher += chr((ord(char) + shift - 65) % 26 + 65)
    else:
        cipher += chr((ord(char) + shift - 97) % 26 + 97)
    print(cipher)