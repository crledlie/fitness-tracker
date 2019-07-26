import os
# We have an application we're going to start, gimme
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

# Defines what's happening in the database
app = Flask(__name__)
app.config.from_object(Config)
# We're using SQL for our database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from fitness_tracker import routes, models

if __name__ == '__main__':
    app.run(debug=True)
