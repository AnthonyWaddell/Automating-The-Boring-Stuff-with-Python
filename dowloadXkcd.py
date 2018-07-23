#! python3
# Download all the xkcd comics

import requests
import bs4
import os

# Get the starting URL
url = 'http://xkcd.com'
# Create folder to store comics in
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    # Download the webpage
    print('Downloading page %s...' % url)
    res = requests.get(url)
    # Make sure the url download worked
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    # Find the URL of the comic image
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could no find comic image...')
    else:
        try:
            comicUrl = 'http:' + comicElem[0].get('src')
            # Download the image.
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            # Make sure the image download worked
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            # Skip this comic
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prevLink.get('href')
            continue
        
        # Save the image to ./xkcd.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(10000):
            imageFile.write(chunk)
        imageFile.close()

    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')


print('Finished downloading all comics from xkcd...')
