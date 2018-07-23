#! python3
""" Simple python script that will and Wikipedia style bullet points to
 	the start of each line of text on the clipboard"""

import pyperclip
text = pyperclip.paste()

# Distinguish each line by splitting and ading stars
lines = text.split('\n')
# For each line
for i in range(len(lines)):
	# Add the * before the content
	lines[i] = '* ' + lines[i]
# assign the new list to text as one string for the clipboard
text = '\n'.join(lines)

pyperclip.copy(text)