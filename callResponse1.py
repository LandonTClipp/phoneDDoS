# This is the script that Twilio uses when calling a number. This script must be passed to Flask to
# generate a local server.

from flask import Flask, request, redirect
from twilio.twiml.voice_response import VoiceResponse, Gather
import time

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    to_number = request.values.get('To', None)
    
    print ( to_number )         # Print the number to the terminal when it picks up 
    resp = VoiceResponse()      # Initialize the VoiceResponse object

    resp.pause(length=30)       # Pause for 30 seconds to give time for the agent to pick up



    response = "This is what Twilio will say when the caller picks up."
    resp.say(response)

    # Wait 1 second before continuing on
    resp.pause(length=1)
    
    # Say it two more times    
    resp.say(response)
    resp.pause(length=1)
    resp.say(response)
    resp.pause(length=1)

    # Exit the call
    return str(resp)
