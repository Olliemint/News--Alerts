from app import app


import urllib.request,json

from .models import news


News = news.News


#getting api key
api_key = app.config["News_api"]

#getting news url
main_url = app.config["news_base_url"]


def get_article(category):
    
    get_news_url = main_url.format(category,api_key)
    
    with urllib.request.urlopen(get_news_url) as url:
        
        get_news_data = url.read()
        
        get_news_response = json.loads(get_news_data)
        
        news_results = None
        
        if get_news_response["results"]:
            
            news_results_list = get_news_response["results"]
            
            news_results = process_results(news_results_list)
        
    return news_results


def process_results(news_list):
    
    """
    function that process results and return list of objexts
    
    """    