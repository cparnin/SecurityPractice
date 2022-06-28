#!/usr/bin/env python3

from distutils.command.install_lib import PYTHON_SOURCE_EXTENSION
import re
from urllib.request import urlopen

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

# Parsing logs function

def logs():
	print("Lets parse the /var/log/system.log on a Mac")
	f = open('/var/log/system.log')
	lines = f.readlines()
	print(lines)
	for line in lines:
		if "error" in line:
			x = line.split("Function:")
			print(line.split()[0],line.split()[1],line.split()[3], " Error message: ", x[1])
	f.close()

#-----------------------

# Web scraping function
def scraping():
	url = "https://dvwa.co.uk/"
	# open the URL
	page = urlopen(url) # Class type: http.client.HTTPResponse
	# read the bytes (text, newlines, img srcs, etc)
	html = page.read().decode("utf-8") # Class type: bytes (read) -> str (utf)

	'''
	# Manual title findin'
	index after <title>
	start_index = html.find("<title>") + len("<title>") # or 7
	print("Starting index of real title (after <title>) " + str(start_index))
	# ending
	end_index = html.find("</title>")
	print("Index at end of title " + str(end_index))
	print("Length of title is: " + str(end_index-start_index))
	# print title
	print("Title: " + str(html[start_index:end_index]))
	'''

	# find the title
	# match any text after <title, up to >
	pattern = "<title.*?>.*?</title.*?>"
	match_results = re.search(pattern, html, re.IGNORECASE)
	title = match_results.group() # give us the most relevant choice (usually what we want)
	title = re.sub("<.*?>", "", title) # sub tags with empty
	print(title)


#-----------------------

# Main

if __name__ == "__main__":
	print("Do you want to talk about feelings, ciphers, logs, or scraping?")
	answer=input("")
	if answer == "feelings":
		feelings()
	elif answer == "ciphers":
		ciphers()
	elif answer == "logs":
		logs()
	elif answer == "scraping":
		scraping()