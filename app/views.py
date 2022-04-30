from flask import render_template
from app import app

#views

@app.route('/')

def home():
    
    return render_template("index.html")