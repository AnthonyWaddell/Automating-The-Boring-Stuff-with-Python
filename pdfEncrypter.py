#! python3
''' Simple python script that goes through a folder and all subfolders and encrypts
	all .pdf files with password provided by command line'''

import PyPDF2
import os
import sys

# Get the password and create list for 
password = sys.argv[1]

# Start from current working directory and iterateover all files/(sub)folders
for root, directory, filename in os.walk('.'):
	# If it's a PDF, we are going to encrypt it
	if filename.endwith('.pdf'):
		# Get the absolute path
		path = os.path.join(root, filename)
		pdfReader = PyPDF2.PdfFileReader(open(path, 'rb'))
		# If it isn't already encrypted
		if pdfReader.isEncrypted is False:
			pdfWriter = PyPDF2.PdfFileWriter()
			for pdf_page in range(pdfReader.numPages):
				pdfWriter.addPage(pdf_reader.getPage(pdf_page))

			# Encrypt this PDF as a copy and save it with _encrypted
			pdfWriter.encrypt(password)
			encrypted_path = (path[:-4] + '_encrypted.pdf')
			encrypted_pdf = open(encrypted_path, 'wb')
			pdfWriter.write(encrypted_version)
			encrypted_version.close()

			 # If it was encrypted properly
			 pdfReader = PyPDF2.PdfFileReader(open(encrypted_path, 'rb'))
			 if pdfReader.isEncrypted:
			 	decrypted = pdfReader.decrypt(password)
			 	if decrypted:
			 		os.remove(path)
			 # If it wasn't encrypted properly
			 else:
			 	print('Failed to encrypt: ' + filename)
			 	print(filename + ' not deleted...')