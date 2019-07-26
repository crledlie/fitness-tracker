# Different endpoints for server, functions, and definitions for logic
from flask import request
from twilio.twiml.messaging_response import MessagingResponse
from fitness_tracker import app, db
# Imports User model from database
from fitness_tracker.models import User

# This points the app towards the ngrok URL and /sms specifically and tells it to put something on it by POSTing
# App.route - basis for app ; whenever anyone goes to this path it'll post the following...
@app.route('/sms', methods=['POST'])
# Defines all of the sms variables
def sms():
    number = request.form['From']
    message_body = request.form['Body']
    # MessagingResponse = We'll send a message no matter what
    response = MessagingResponse()
    user = User.query.filter_by(phone_number = number).first()
    print(user)
    if user is None: 
        # Moves user to next page after text is sent
        response.message('Welcome to the Fitness Tracker! What\'s your name?', action='/onboarding1', method='POST')
    else:
        response.message('Good to see you again username, starting your "message_body" workout now!', action='/endworkout', method='POST')     
    return str(response)
# Boilerplate
@app.route('/onboarding1', methods=['POST'])
def onboarding1():
    number = request.form['From']
    message_body = request.form['Body']
    user = User(username = message_body, phone_number = number)
    db.session.add(user)
    db.session.commit()
    response = MessagingResponse()
    response.message('Good to meet you {}').format(message_body)
    return str(response)

@app.route('/endworkout', methods=['POST'])
def endworkout():
    response = MessagingResponse()
    response.message('Great workout! You worked out for x amount of time!')
    return str(response)