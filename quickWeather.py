#! python3
''' take input from command line and prints the weather for a given location
	in plaintext. Uses openweathermap.org

	example command line: quickWeather.py Seattle, WA'''

import json
import sys
import requests

# Get the location from the command line
if len(sys.argv) < 2:
	print('Usage: quickWeather.py. Requires: location')
	sys.exit()
location = ' '.join(sys.argv[1:])

# Downlod the JSON data from OpenWeatherMap.org's API
url ='http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)
response = requests.get(url)
response.raise_for_status()

# Get the JSON data in a python variable
weatherData = json.loads(response.text)

# Print the weather description, use a dictionary for each day
w = weatherData['list']
print('CUrrent weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])