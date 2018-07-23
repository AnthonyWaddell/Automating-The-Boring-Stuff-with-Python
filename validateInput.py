"""Program to validate input, from Automate the Boring Stuff
Chapter 6: String MAnipulation"""

# Gather user age
while True:
	print('Please enter your age:')
	age = input()
	if age.isdecimal():
		break
	print('Age must be a number, please enter a number')

# Gather user password
while True:
	print('Please input a password with letters and nmumber only:')
	password = input()
	if password.isalnum():
		break
	print('Password must consist of letters and numbers only')
