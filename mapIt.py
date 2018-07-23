#! python3

''' Launches a map in the browser using an address from the command line or 
	clipboard
	Sample command: mapit 14701 Cascadian Way, Lynnwood, WA 98087
	'''

import webbrowser
import sys
import pyperclip

# If there is anything from the command line
if len(sys.argv) > 1:
	# Get address from command line
	address = ' '.join(sys.argv[1:])
else:
	# Grab the address from the clipboard
	address = pyperclip.paste()

# Open the web browswer and search google maps for the address
webbrowser.open('https://www.google.com/maps/place/' + address)