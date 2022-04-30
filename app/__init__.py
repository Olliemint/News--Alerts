#used to create an app instance
from flask import Flask

#initializing news app

app = Flask(__name__)

#allow us create views

from app import views