""" 
this module is where the flask instance and database live. 
It's imported in a lot of other places, so keep it thin to
avoid circular imports
"""

from flask import Flask
import os

app = Flask(__name__)
#app.config.from_object(os.environ['APP_SETTINGS'])
