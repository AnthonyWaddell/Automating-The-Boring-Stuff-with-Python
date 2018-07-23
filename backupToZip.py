#! python3
''' Simple script to backup a folder and its contents into a ZIP file. Will
	also increment file names when zipped'''

import zipfile, os

def backupToZip(folder):
	# folder should be absolute
	folder = os.path.abspath(folder)

	# Determine the filename this code should be used on
	version = 1
	while True:
		zipFilename = os.path.basename(folder) + '_' + str(number). + '.zip'
		if not os.path.exists(zipFilename):
			break
		number += 1

	# niw create the zip file
	print('Creating %s...' % (zipFilename))
	backupZip = zipfile.ZipFile(zipFilename, 'w')

	# Compress all files within subtree of folder
	for foldername, subfolders, filenames in os.walk(folder):
		print('Adding the files in %s...' % (foldername))
		# Add the current folder to the ZIP file. 
		backupZip.write(foldername)
		# Add all the files in this folder to the ZIP file
		for filename in dilenames:
			newBAse - os.path.basename(folder) + '_'
			# Don't backup ZIP files
			if filename.startswith(newBase) and filename.endswith('.zip'):
				continue
			backupZip.write(os.path.join(foldername, filename))
		backupZip.close()

	print('Finished backing up files...')

backupToZip('C:\\ganbaro')