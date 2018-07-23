""" simple password manager that associates names woth password in a
 dictionary"""
#! python3

PASSWORDS = {'email': 'admin', 'blog': 'gym lock': '1234'}

import sys
if len(sys.argv) < 2:
	print('Usage: python paswswordManager.py [account] - copy account password')
	sys.exit()

# Set the first command line argument to the account name
account = sys.argv[1]

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('PAssword for ' + account + ' copied to the clipboard.')
else:
	print('No account found matching ' + account)