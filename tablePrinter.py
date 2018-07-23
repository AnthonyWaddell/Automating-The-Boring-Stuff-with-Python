"""Write a function named printTable() that takes a list of lists of 
strings and displays it in a well-organized table with each column 
right-justified. Assume that all the inner lists will contain the same 
number of strings. For example, the value could look like this:


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
Your printTable() function would print the following:


  apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose"""

# TAble to format
tableData=[['apples', 'oranges', 'cherries', 'banana'], 
['Alice', 'Bob', "Carol", "David"],
 ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):

	# To get length of longest line
	longest = 0
	# For every line
	lines = []

	# For each item in the inner list
	for items in zip(tableData[0], tableData[1], tableData[2]):
		# Join the items into one string
		line = ' '.join(items)
		# Add that string to the list of strings
		lines += line
		# Keep track of the longest line
    	length = len(line)
    	if length > longest:
			longest = length

	# Output the table
	longest += 1
	for line in lines:
		print('%*s' % (longest, line))

printTable(tableData)