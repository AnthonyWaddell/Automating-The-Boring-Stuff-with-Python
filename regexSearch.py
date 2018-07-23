''' Simple script to allow a user to search for a term/text/string within all 
	files in a directory. Return a list of all matching occurences of the
	user defined search term.'''

import re, os

def fileSearch():
	# To store the matches
	matchList = []
	# Iterate over all files
	for files in allFiles:
		myFileObject = open(os.path.abspath(files), errors = 'ignore')
		myFileContent = myFileObject.read()
		matchList += searchRegex.findall(myFileContent)
		myFileObject.close()
	return matchList   

 # Gather what the user wants to look for
print("What text would you like to search your documents for?")
searchRegex = re.compile(input())

# Get list of all files within directory
allFiles = os.listdir()
# Gather list of all found matching items
return_list = fileSearch()
# Display the matching items
print(return_list)