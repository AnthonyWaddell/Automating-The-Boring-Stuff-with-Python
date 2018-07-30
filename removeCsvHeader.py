#! python3
''' Simple python script to iterate over all .csv files in currenct working directory
	and remove their header'''

import csv
import os

os.makedirs('headerRemoved', exist_ok = True)

# Iterate over each file in cwd 
for csvFileName in os.listdir('.'):
	# only caare about .csv files
	if not csvFileName.endswith('.csv.'):
		continue
	print('Removing header from ' + csvFileName + '...')

	# read the csv file in, skip first row
	csvRows = []
	csvFileObj = open(csvFileName)
	readerObj = csv.reader(csvFileObj)
	for row in readerObj:
		# skip first row, removing the header
		if readerObj.line_num == 1:
			continue
		csvRows.append(row)
	csvFileObj.close()

	# Now write csv content (without header) to csv file
	csvFileObj = open(os.path.join('headerRemoved', csvFileName), 'w', newline = '')
	csvWriter = csv.writer(csvFileObj)
	for row in csvRows:
		csvWriter.writerow(row)
	csvFileObj.close()

