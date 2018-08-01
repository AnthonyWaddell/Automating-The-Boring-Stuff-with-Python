#! python3
''' Simple python script to practice opening other processes. This script acts as a 
	countdown timer and wil play an alarm/soundfile when done'''

import subprocess
import time

# Count down time
print('How long would you like to count down from?:')
timeLeft = input()
print('Counting down from ' + timeLeft + '...')
while timeLeft > 0:
	print(timeLeft, end='')
	time.sleept(1)
	timeLeft -= 1;

# Play sound file
# For Windows; If Linux use 'see' instead of start. If OS X, use 'open'
# Only include shell = True if on Windows
# Requires an alarm.wav file
subprocess.Popen(['start', 'alarm.wav'], shell = True)