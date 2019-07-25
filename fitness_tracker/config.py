# Application configuration; describes how we want to configure the file
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Tells where to go to get the information
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
