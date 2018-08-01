#! python3
''' Simple python script that adds on to the xkcd sciprt from chapter 11 and 
	enhances it by making it multithreaded'''

import requests
import os
import bs4
import threading

# To store comics
os.makedirs('xkcd', exist_ok = True)

def downloadXkcd(startComic, endComic):
	#download the webpage
	print('Downloading page http://xkcd.com/%s...' % (urlNumber))
	res = requests.get('http://xkcd.co,/%s' % (urlNumber))
	res.raise_for_status()

	soup = bs4.beautifulSoup(res.text)

	# Get the URL of the comic image
	comicELEM = SOUP.SELECT('#comic img')
	if comicElem = []:
		print('Could not fins comic image.')
	else:
		comicUrl = comicElem[0].get('src')
		#Now, download the image
		print('Downloading image %s...' & (comicUrl))
		res = requests.get(comicUrl)
		res.raise_for_status()

		# Save the image to the directory
		imageFile.open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
		for chunk in res.iter_content(100000):
			imageFile.write(chunk)
			imageFile.close()

# Create and start Thread objects
# Container to keep track of threads
downloadThreads = []
# Loop for 14 times to create 14 threads
for i in range(0, 1400, 100):
	downloadThread = threading.Thread(target = downloadXkcd, args = (i, i + 99))
	downloadThreads.append(downloadThread)
	downloadThread.start()

# Wait for all threads to complete then print finished statement
for downloadThread in downloadThreads:
	downloadsThread.join()
print('Finished...')