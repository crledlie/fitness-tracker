# Different endpoints for server, functions, and definitions for logic
import ipdb
import datetime
from flask import request
from twilio.twiml.messaging_response import MessagingResponse
from fitness_tracker import app
# Imports User model from database
from fitness_tracker.models import User, LoggedWorkout
from fitness_tracker.manage import db


# This points the app towards the ngrok URL and /sms specifically and tells it to put something on it by POSTing
# App.route - basis for app ; whenever anyone goes to this path it'll post the following...
@app.route('/user', methods=['POST'])
# Defines all of the sms variables
def user():
    print(request.form)
    number = request.form['From']
    message_body = request.form['Body']
    # MessagingResponse = We'll send a message no matter what
    # response = MessagingResponse()
    user = User.query.filter_by(phone_number = number).first()
    print(user)
    if user is None: 
        # Moves user to next page after text is sent
       # response.message('Welcome to the Fitness Tracker! What\'s your name?', action='/onboarding1', method='POST')
       return str('Welcome to the Fitness Tracker! What\'s your name?')
    else:
        # response.message('Good to see you again username, starting your "message_body" workout now!', action='/endworkout', method='POST')     
        return str('Good to see you again!')
# Boilerplate
@app.route('/onboarding', methods=['POST'])
def onboarding():
    name = request.form['name']
    email = request.form['email']
    number = request.form['number']
    user = User(username = name, phone_number = number, email = email)
    db.session.add(user)
    db.session.commit()
    return str(user)

@app.route('/workout', methods=['GET', 'POST'])
def workout():
    number = request.form['number']
    user = User.query.filter_by(phone_number = number).first()
    print(user)
    def check_workout_status(workout):
        if workout.end_time is None:
            return True
        else:
            return False
    if request.method == 'GET':
        return user.is_working_out

    if request.method == 'POST':
        if user.is_working_out:
            ipdb.set_trace()
                # TODO: Should we use filter or filter_by from SQLalchemy?
                # Find active work out status 
            active_workout=filter(check_workout_status, user.logged_workouts)
            print(active_workout[0])
            active_workout[0].end_time=datetime.datetime.now()
            print(active_workout[0])
            # function that commits end work out time
            db.session.commit()
            return str('Workout ended')
        else:
            workout = request.form['workout_type']
            logged_workouts = LoggedWorkout(user_id = user.id, workout_type = workout, start_time = datetime.datetime.now())
            db.session.add(logged_workouts)
            db.session.commit()
            return str('Starting workout')

@app.route('/endworkout', methods=['POST'])
def end_workout():
    print(request.form)
    # response = MessagingResponse()
    # response.message('Great workout! You worked out for x amount of time! Come back soon!')
    # TODO: Update database; logged workout needs an end time 
    return str('Great workout! You worked out for x amount of time! Come back soon!')