# Different endpoints for server, functions, and definitions for logic
from flask import request
from twilio.twiml.messaging_response import MessagingResponse
from fitness_tracker import app

# This points the app towards the ngrok URL and /sms specifically and tells it to put something on it by POSTing
# App.route - basis for app ; whenever anyone goes to this path it'll post the following...
@app.route('/sms', methods=['POST'])
# Defines all of the sms variables
def sms():
    number = request.form['From']
    message_body = request.form['Body']
    response = MessagingResponse()
    response.message('Hello {}, you said: {}'.format(number, message_body))
    return str(response)
