#! python3
''' Simple python scipt to act as a stopwatch, great if you don't want to download
	that has a ton of ads and sends a copy of your browser history to marketers.'''

import time

# Prompt the user
print('Press the ENTER key to begin. When finished, press the ENTER key again \
	to stop. Press CTRL-C to quit.')
input()
print('Started...')
startTime = time.time()
lastTime = startTime
lapNum = 1

# Begin tracking lap times
try:
	while True:
		input()
		lapTime = round(time.time() - lastTime, 2)
		totalTime - round(time.time() - startTime, 2)
		print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
		# Increment the lap and reset the lap timer
		lapNum += 1
		lastTime = time.time() 
except KeyboardInterrupt:
	# Handle end case
	print('Done...')