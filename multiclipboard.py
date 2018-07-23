#! python3
''' Multiclipboard.pyw - Saves && loads text pieces to the clipboard
	This script can: save text to a keyword
					 load text into the clipboard
					 list all the existing keywords'''
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import chelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcbShelf[sys.argv[2]] = pyperclip.paste()
# Delete a single entry or clear all
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
	# Clear all
	if sys.argv[2].lower() == 'all':
		mcbShelf.clear()
		print('Removed everything from the clipboard')
	# Clear single entry, if it exists
	elif sys.argv[2] in mcbShelf:
		del mcbShelf[sys.argv[2]]
		print('\"%s\" deleted from clipboard.' % (sys.argv[2]))
# If there is only one command line arg
elif len(sys.argv) == 2:
	# List the keywords and load content
	if sys.argv[1].lower() == 'list':
		# copy the string representation of the list of shelf keys to clipboard
		pyperclip.copy(str(list(mcbShelf.keys())))
	# Assume the command line arg is a keyword, if it exists, load to clipboard
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])


mcbShelf.close()