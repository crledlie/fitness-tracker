from flask import request
from twilio.twiml.messaging_response import MessagingResponse
from fitness_tracker import app

@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']
    response = MessagingResponse()
    response.message('Hello {}, you said: {}'.format(number, message_body))
    return str(response)
