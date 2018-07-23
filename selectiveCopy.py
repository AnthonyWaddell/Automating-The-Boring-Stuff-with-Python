#!python

''' Simple python script to walk over a directory && it\'s subtree and copy 
	all files with given file extension (in this, .pdf) to a new folder.'''

import os, shutil

def selectiveCopy(folder):
	print('Please enter the file extension you wish to copy all files of (without .): ')
	extension = input()
	extension = '.' + extension
	# get the absolute path of the folder
    folder = os.path.abspath(folder)
    # iterate over all files/subfolders
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if not filename.endswith(extension):
                continue
            #shutil.copy(filename, 'C:\\pdffolder') # commented for safety
            print('Copying ' + filename + ' to new folder...') 

selectiveCopy(r'C:\\Users\\cur_user\\pdffolder') # replace cur_user with actual user folder
print('DFinished copying all files ending with ' + extension + '...')