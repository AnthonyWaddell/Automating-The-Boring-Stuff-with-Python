#! python3
''' Simple python script that iterates over folders and files in a directory
	and will look for large files to remove'''


import os

def deleteUnneeded(folder):
	# Get the absolute path for the folder
    folder = os.path.abspath(folder)
    # Iterate over all files/subfolders
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            fileSize = os.path.getsize(foldername + '/' + filename)
            if int(fileSize) < 10000000:
                continue
            # This will delete, commenting to prevent accidents
            print('File: ' + filename + ' found of size: ' + filesize)
            print('Would you like to delete? (Y/N): ')
            deleteFile = input()
            if deleteFile.upper() == 'Y':
            	#os.remove(filename) 
            	print('Deleting ' + filename + '...') 

deleteUnneeded('/Users/username/Documents') #replace username with user account
print('Finished removing large files)