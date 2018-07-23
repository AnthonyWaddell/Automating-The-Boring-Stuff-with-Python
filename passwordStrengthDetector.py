''' Program that takes a string and determines if it would make a strong password
	or not, A strong password is defined as one that is:
	- at least 8 characters
	- ontains both uppercase and lowercase characters
	- has at least one digit'''

import re


passwordRegex = re.compile(r'''(
    ^(?=.*[A-Z].*[A-Z])                # at least two capital letters
    (?=.*[!@#$&*])                     # at least one of these special characters
    (?=.*[0-9].*[0-9])                 # at least two numeric digits
    (?=.*[a-z].*[a-z].*[a-z])          # at least three lower case letters
    .{10,}                              # at least 10 total digits
    $
    )''', re.VERBOSE)

def userInputPasswordCheck():
    ppass = input("Enter your password: ")
    mo = passwordRegex.search(ppass)
    if not mo:
        print("Password is not strong")
        return False
    else:
        print("PAssword is strong")
        return True


userInputPasswordCheck()
