#!/usr/bin/env python3


#####################  READ ME  ###########################
# This is practice for a Security Engineer Google Interview
# Based on Grace Nolan's GitHub Page
# I simply made each topic into functions
# Choose a function to begin
# Comments preceed the line they're referring to
############################################################  


print("\n\nHello, this is my brush up and practice arena\n\n")
name = input("What's your name? ")


#----------------------- FUNCTION DECLARATIONS -----------------------

# Feelings function: Text to emojis

def feelings():
	# initiate the conversation
	print("How do you feel today? (I feel happy/sad)")
	message = input(">")
	# split on the space
	words = message.split(' ')
	print("Printing word list")
	print(words)
	# emoji dictionary
	emojis = {
		"happy":"😀",
		"sad":"🥲"
	}
	# set empty string
	output = ""
	# loop through.  When it finds your key, it returns the value
	for word in words:
		output += emojis.get(word, word) + " "
		print(word)
	print(output)

#-----------------------

# Cipher function

# chr() converts an Integer (ASCII) to a Character
# ord() converts a Character to an Integer (ASCII)
# convert chars to Integers/ASCII to get a baseline
def ciphers():
	print("Welcome to Caesar's Cipher (I know...I know...the easiest...for now)")
	print("Enter text to encrypt")
	text = input()
	print("Shift amount?")
	# need to convert user input: str to int
	shift = int(input())
	cipher = ""
	# iterate through the text
	for i in range(len(text)):
		char = text[i]
		# encrypt uppercase
		if (char.isupper()):
			cipher += chr((ord(char) + shift - 65) % 26 + 65)
		else:
			# encrypt lowercase
			# mod:  if right num > left num, answer is left num
			# 24 % 26 = 24
			# subtract and mod handles edge cases in ASCII Table
			# example for each char: str t into int/ASCII (116),
			# + shift 5 (121), -97 (24), mod 26 (24), + 97 (121),
			# cast back to char/string   
			cipher += chr((ord(char) + shift - 97) % 26 + 97)
			print(cipher)
	print("Your Caesar Cipher encrypt of " + text + " with a shift of " + str(shift) + " is: " + cipher)

#-----------------------

print("Do you want to talk about feelings or ciphers?")
answer=input("")
if answer == "feelings":
	feelings()
elif answer == "ciphers":
	ciphers()
