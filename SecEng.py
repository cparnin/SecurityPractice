#!/usr/bin/env python3

from multiprocessing.connection import Client
import sys
import re
import requests
import socket, subprocess, sys # port scanning
import pyfiglet  # pretty output
from datetime import datetime
from pexpect import pxssh


#####################  READ ME  ###########################
# Security Engineer Playground
# Each topic is a function
# Choose a function to begin
############################################################  

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
	text = input("Enter text to encrypt")
	shift = int(input("Shift amount?"))
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
	
#-----------------------

# Prime number function
def primes():
	num = int(input("Enter number: "))
	flag = 0
	if (num < 2):
		print("Number must be at least 2 (first prime number)")
	else:
		for i in range(2,num):
			if (num % i) == 0:
				print(num, "is not prime")
				flag = 0
				break
			elif (num % i) != 0:
				flag = 1
				continue
	if (flag == 1):
		print(num, "is prime")

#-----------------------

# Word frequency function
def words():
	str = input("Enter phrase")
	str_split = str.split()
	search_word = input("Word to search? ")
	i = 0
	count = 0
	for word in str_split:
		if (search_word == str_split[i]):
			print("Found it at index",i)
			count += 1
		i += 1
	print("Found", count, "occurences of", search_word)	

#-----------------------

# APIs function

def apis():
	'''
	GET:    Retrieve data
	PUT:    Replace data
	POST:   Create data
	DELETE: Delete data
	'''
	print("HTTP GET request\n")
	response = requests.get("http://api.open-notify.org/astros.json")
	print("Here are the astronauts currently in space\n\n",response.json())

	print("HTTP PUT request (update)")
	resource = requests.put('https://httpbin.org/put', data = {'key':'value'})

	print("HTTP POST request (create new)")
	response = requests.post("https://httpbin.org/post", data = {'key':'value'})

#-----------------------

# Stack function
def stacks():
	stack = []
	print("Initial stack: ", stack)
	# PUSH (append)
	stack.append('a')
	print("Stack push: ", stack)
	stack.append(5)
	print("Stack push: ", stack)

	# POP
	stack.pop()
	print("Stack pop: ", stack)

#-----------------------

# Botnet function
def botnets():
	bot_net = []
	class Client:
		def __init__(self, host, user, password): # Class constructor
			self.host = host
			self.user = user
			self.password = password
			self.session - self.connect()
		def connect(self): #connect method
			try: # test connection
				s = pxssh.pxssh()
				s.login(self.host, self.user, self.password)
				return s # if login worked
			except Exception as e: # if failed
				print(e)
				print("Error connecting")
		def send_command(self, cmd):
			self.session.sendline(cmd)
			self.session.prompt()
			return self.session.before # return results
		def botnet_command(command): # send command function
			for client in bot_net:
				output = client.send_command(command) # get output
				print("Output from " + client.host)
				print(output)
		def add_client(host, user, password): # add client to notnet
			client = Client(host, user, password)
			bot_net.append(client) # add client session to botnet

#-----------------------

# Main

if __name__ == "__main__":
	subprocess.call('clear', shell=True) # clear the screen
	print("Do you want to talk about feelings, ciphers, logs, scraping, ports, primes, words, apis, stacks, or botnets?")
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
	elif answer == "primes":
		primes()
	elif answer == "words":
		words()
	elif answer == "apis":
		apis()
	elif answer == "stacks":
		stacks()
	elif answer == "botnets":
		# connection errors - moving on...
		client = Client("127.0.0.1", "user", "pass")
		client.add_client()
		client.botnet_command("ls -al")
	else:
		print("Did not enter correct option.  Exiting")