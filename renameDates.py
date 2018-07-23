#1 python3
''' Simple python script that scans all ffiles in directory looking for 
	dates formatting in the American style to replace with dates formatted in
	a European style'''

import shutil, os, replace

# Regex for American style format
datePattern = re.compile(r"""(.*?)) # all the text before the date
	((0|1)?\d)-                        # one or two digits for the month
	((0|1|2|3)?\d)-                    # one or two digits for the day
	((19|20)\d\d)                      # four digits for the year
	(.*?)$                             # all the text after the date
	""", re.VERBOSE)

# Check all files in the current working directory
for americanFilename in os.listdir('.'):
	mo = datePattern.search(americanFilename)

	# Skip files that do not include a date. 
	if mo == None:
		continue

	# If they include a date, parse it
	beforeDate = mo.group(1)
	monthPortion = mo.group(2)
	datePortion = mo.group(4)
	yearPortion = mo.group(6)
	afterDate = mo.group(8)

	# Use the parsed date information to make a Euro-style date
	euroFileName = beforeDate + datePortion + '-' + monthPortion + '-' + yearPortion + afterDate

	# Get the absolute file paths.
	absWorkignDir = os.path.abspath('.')
	americanFilename = os.path.join(absWorkignDir, americanFilename)
	euroFileName = os.path.join(absWorkignDir, euroFileName)

	# Rename the files
	print('Renaming "%s" to "%s"...' % (americanFilename, euroFileName))
	#shutil.move(americanFilename, euroFileName) # remove this comment after testing