#! python3
''' Simple python script to find all files with a .pdf in the working directory
	and combine them all into a single PDF document without every cover page.'''

import PyPDF2
import os

# Get all the PDF file names
pdfFiles = []
# Get list of every file in the current working directory
for filename in os.listdir('.'):
	# If a file ends with .pdf
	if filename.endswith('.pdf'):
		# Add it to the list 
		pdfFiles.append(filename)
# Get the list in alphabetical order
pdfFiles.sort(keys=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

# Go over every PDF file
for filename in pdfFiles:
	pdfFileObj = open(filename, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

	# Go over every page besides the first page and add them to combined PDF
	for pageNum in range(1, pdfReader.numPages):
		pageObj = pdfReader.getPage(pageNum)
		pdfWriter.addPage(pageObj)

# Save the combined PDF file to a file
pdfOutput = open('allFiles.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()