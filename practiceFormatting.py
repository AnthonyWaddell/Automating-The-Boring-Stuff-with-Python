""" Practicing using string manipulation to format data output"""

# Function to print in a specified format
def printPicnic(inventory, left_width, right_width):
	print('PICNIC ITEMS'.center(left_width + right_width, '-'))
	for i, j in inventory.items():
        print(i.ljust(left_width, '.') + str(j).rjust(right_width))

# Instantiate the dictionary of items and practice printing    
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)