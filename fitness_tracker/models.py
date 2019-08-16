# Database models; what objects exist in our application
from fitness_tracker.manage import db, app

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    # (64) is maximum character length, needs to be unique so there are no duplicates
    username = db.Column(db.String(64), index=True, unique=True)
    phone_number = db.Column(db.String(120), index=True, unique=True)
    # Does not need to be unique
    is_working_out = db.Column(db.Boolean,default=False)
    email = db.Column(db.String, index=True)
    # Knows the relationship between LoggedWorkout exists; Lazy load: only pulls in data...? (Google me)
    logged_workouts = db.relationship('LoggedWorkout', backref='users', lazy=True)

    def __repr__(self):
        return '<User %r>' % (self.username)


class Workout(db.Model):
    __tablename__ = 'workouts'

    id = db.Column(db.Integer, primary_key=True)
    # (64) is maximum character length, needs to be unique so there are no duplicates
    type = db.Column(db.String(64), index=True, unique=True)
    is_strength = db.Column(db.Boolean)
    # Does not need to be unique
    is_cardio = db.Column(db.Boolean)
    is_flexibility = db.Column(db.Boolean)

    def __repr__(self):
        return '<Workout %r>' % (self.workouts)

class LoggedWorkout(db.Model):
    __tablename__ = 'loggedworkout'

    id = db.Column(db.Integer, primary_key=True)
    # Pulls user's id from User table using "db.Foreignkey"
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # Uses Python's DateTime object to log the date and time
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    workout_type = db.Column(db.String(64))

    def __repr__(self):
        return '<LoggedWorkout %r>' % (self.workout_type)    
