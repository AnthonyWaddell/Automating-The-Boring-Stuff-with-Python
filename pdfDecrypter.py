!# python3
''' Simple python script to iterate over all folders, subfolders, and files
	in current working directory and if they are encrypted with password
	passed in as command line arguement, will decrypt them.'''

import PyPDF2
import os
import sys

# Get the password and create list for 
password = sys.argv[1]

# Start from current working directory and iterateover all files/(sub)folders
for root, directory, filenames in os.walk('.'):
	# If it's a PDF, we are going to encrypt it
	if filename.endwith('.pdf'):
		# Get the absolute path
		path = os.path.join(root, filename)
		pdfReader = PyPDF2.PdfFileReader(open(path, 'rb'))
		# If it isn't already encrypted
		if pdfReader.isEncrypted is True:
			decrypted = pdfReader.decrypt(password)
			if decrypted:
				pdfWriter = PyPDF2.PdfFileWriter()
				for pdf_page in range(pdfReader.numPages):
					pdfWriter.addPage(pdfReader.getPage(pdf_page))

				# Save a copy of the pdf with decrypted added to file name
				decryptedPath = (path[:-4] + '_decrypted.pdf')
				decryptedPdf = open(decryptedPath, 'wb')
				pdfWriter.write(decryptedPdf)
				decryptedPdf.close()
			else:
				print('Failed to decrypt: ' + filename)
			 	print(filename + ' not deleted...')