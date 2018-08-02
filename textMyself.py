#! python3
""" Simple python script with a funtion that can be used to text myself. Requires
	user to set up a Twilio account and to have their account SID, their authorization
	toke, their Twilio number, and a valid cell phone number. Put this file in any 
	folder as the Python executable and import textMyself"""

# example: textMyself.textmyself('Some message')

from twilio.rest import TwilioRestClient

# My information
accountSID = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
authToken = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
myNumber = '+1234567890'
twilioNumber = '+0987654321'

def textmyself(message):
	twilioCli = TwilioRestClient(accountSID, authToken)
	twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)