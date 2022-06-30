#!/usr/bin/env python3

from urllib.request import urlopen
import re
import socket, subprocess, sys # port scanning
import pyfiglet  # pretty output
from datetime import datetime

#####################  READ ME  ###########################
# Security Engineer Playground
# Each topic is a function
# Choose a function to begin
############################################################  

print("\n\nHello, this is my practice arena\n\n")
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
	title = re.sub("<.*?>", "", title) # sub tags with empty str
	print(title)

#-----------------------

# Port Scanning function
def ports():
	banner = pyfiglet.figlet_format("PORT SCANNER")
	print(banner)

	target = "T76W9XCDR6.local"
	
	# banner
	print("-" * 50)
	print("Scanning target: " + target)
	print("Scan started at: " + str(datetime.now()))
	print("-" * 50)

	try:
		for port in range(1,100):
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # opening a IPv4, TCP socket
			socket.setdefaulttimeout(.5)
			result = s.connect_ex((target,port)) # connect to the port
			if result == 0: # 0 is open
				print("Port {} is open".format(port))
			s.close()
	except KeyboardInterrupt:
		sys.exit("Ctrl-C entered")
	except socket.gaierror: # get address info error
		print("Hostname can't be resolved.  Exiting")
	except socket.error:
		sys.exit("Can't connect to server")
	
	'''
	#OLD
	t1 = datetime.now()
	#server = input("Enter a host to scan (FQDN): ")
	server = "T76W9XCDR6.local"
	ip = socket.gethostbyname(server)
	try:
		for port in range (79,81):
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # opening a IPv4, TCP socket
			result = sock.connect_ex((server, port)) # connect to the server port
			if result ==0:
				print("Port {}: Open".format(port))
			sock.close()
	except KeyboardInterrupt:
		sys.exit("Ctrl-C entered")
	except socket.gaierror: # get address info error
		print("Hostname can't be resolved.  Exiting")
	except socket.error:
		sys.exit("Can't connect to server")
	t2 = datetime.now()
	t_total = t2-t1
	print("Hostname: " + server + "\nIP: " + ip + "\nTime to scan: " + str(t_total))
	'''

#-----------------------

# Botnet function
def botnets():
	


#-----------------------

# Main

if __name__ == "__main__":
	subprocess.call('clear', shell=True) # clear the screen
	print("Do you want to talk about feelings, ciphers, logs, scraping, ports, or botnets?")
	answer=input("")
	if answer == "feelings":
		feelings()
	elif answer == "ciphers":
		ciphers()
	elif answer == "logs":
		logs()
	elif answer == "scraping":
		scraping()
	elif answer == "ports":
		ports()
	elif answer == "botnets":
		ports()