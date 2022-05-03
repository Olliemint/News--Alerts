#used to create an app instance
from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap


#initializing news app

app = Flask(__name__,instance_relative_config= True)


#setting configuration 

app.config.from_object(DevConfig)

app.config.from_pyfile("config.py")

#allow us create views

from app import views