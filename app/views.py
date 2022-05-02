
from unicodedata import category
from flask import render_template
from app import app
from .request import get_article,get_sources


#views

@app.route('/')

def index():
    '''
    returns home page and its data
    '''
    
    news = get_article()
    
    sources= get_sources()
    print(sources)
    
    
    
    return render_template("index.html",news=news,sources = sources)