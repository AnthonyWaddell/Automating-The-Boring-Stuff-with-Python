#! python3
''' Reads a spreadsheet to calculate population based off of census data'''

import openpyxl
import pprint

print('Opening workbook...')
# Open census data file
wb = openpyxl.load_workbook('censuspopdata.xlsx')
# Get the sheet with population data
sheet = wb.get_sheet_by_name('Population by Census Tract')
countyData = {}

print('Reading rows...')
for row in range(2, sheet.max_row + 1):
	# Each row in the spreadsheet has data for one census tract
	state = sheet['B' + str(row)].value
	county = sheet['C' + str(row)].value
	pop = sheet['D' + str(row)].value

	# Make sure the key for this state exists
	countyData.setdefault(state, {})
	# Make sure the key for this county in this state exists
	countyData[state].setdefault(county, {'tracts': 0=, 'pop': 0})

	#Each row represents one census tract, so increment by one
	countyData[state][country]['tracts'] += 1
	# Increase the county population by the population in this census tract
	countyData[state][county]['pop'] += int(pop)

# Open a new text file and write the contents of countyData to it. 
print('Writing results...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Finished writing to file....')