# Different endpoints for server, functions, and definitions for logic
import datetime
from flask import request, jsonify
from fitness_tracker import app
# Imports User model from database
from fitness_tracker.models import User, LoggedWorkout
from fitness_tracker.manage import db


# This points the app towards the ngrok URL and /sms specifically and tells it to put something on it by POSTing
# App.route - basis for app ; whenever anyone goes to this path it'll post the following...
@app.route('/user', methods=['POST'])
# Defines all of the sms variables
def user():
    number = request.form['From']
    message_body = request.form['Body']
    # MessagingResponse = We'll send a message no matter what
    # response = MessagingResponse()
    user = User.query.filter_by(phone_number = number).first()
    if user is None:
       return jsonify({
        "user_id": None,
        "message": 'Welcome to the Fitness Tracker! What\'s your name?'
       })
    else:
        return jsonify({
            "message": 'Good to see you again!',
            "username": user.username,
            "user_id": user.id
        })

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
    current_user = User.query.filter_by(phone_number = number).first()
    if request.method == 'GET':
        return jsonify({
            "is_working_out": current_user.is_working_out
        })

    if request.method == 'POST':
        if current_user.is_working_out:
            current_user.is_working_out = False
            end_workout_time = datetime.datetime.utcnow()
            active_workout = LoggedWorkout.query.filter_by(end_time=None, user_id=current_user.id).first()
            active_workout.end_time = end_workout_time
            db.session.commit()
            date_diff = end_workout_time - active_workout.start_time
            return jsonify({
                "workout_type": active_workout.workout_type,
                "duration": date_diff.total_seconds() / 60
            })
        else:
            current_user.is_working_out = True
            workout_start = datetime.datetime.utcnow()
            current_workout = request.form['workout_type']
            logged_workout = LoggedWorkout(user_id=current_user.id, workout_type=current_workout, start_time=workout_start)
            db.session.add(logged_workout)
            db.session.commit()
            return str('Starting workout')
