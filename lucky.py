#! python3
''' Simple python script that takes a search term from the command line and 
	opens several search results from Google.'''

import requests
import sys
import webbrowser
import bs4

# Display text so user knows its working
print('Googling...')
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Get the top search results
soup = bs4.BeautifulSoup(res.text)

# Open a new tab for each result, default will be the first 5
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
	webbrowser.open('http://google.com' + linkElems[i].get('href'))