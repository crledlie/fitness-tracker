# Imports from flask library/framework + request module (way to interact with request you're receiving on server)
from flask import Flask, request
# Importing helper library from where you put twilio API; imports twilio markdown language
from twilio.twiml.messaging_response import Message, MessagingResponse

# Defines the variable called app with value flask
app = Flask(__name__)

# Envokes the app and adds a route to it (ie: localhost); creates path (/sms); method: (endpoint) post - people can create things
@app.route('/sms', methods=['POST'])
# Everything after the colon will be executed every time you do the function "sms"
def sms():
    # gets the from phone number and assigns it to number
    number = request.form['From']
    # gets the body paramater and assigns it to message_body <- snake case 
    message_body = request.form['Body']
    # creates response in twiml and assigns it to resp 
    response = MessagingResponse()
    # adds a tag inside of the response that says the message with .message; .format {}s with number and message_body
    response.message('Hello {}, you said: {}'.format(number, message_body))
    # returns the response; str: turns it into a string
    return str(response)
# runs the app
if __name__ == '__main__':
    app.run()