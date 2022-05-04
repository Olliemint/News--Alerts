from flask import render_template
from .import main
from ..request import get_article,get_sources


#views

@main.route('/')
def index():
    '''
    returns home page and its data
    '''
    
    news = get_article()
    
    sources= get_sources()
    
    
    
    
    return render_template("index.html",news=news,sources = sources)