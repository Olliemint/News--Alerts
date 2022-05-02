

from app import app


import urllib.request,json


from .models import news,source


Articles = news.Articles

Source = source.Source



#getting api key
api_key = app.config['NEWS_API_KEY']

#getting news url
main_url = app.config['BASE_URL']

source_url = app.config['SOURCE_URL']


def get_article():
    
    get_news_url = main_url.format(api_key)
    
    with urllib.request.urlopen(get_news_url) as url:
        
        get_news_data = url.read()
        
        get_news_response = json.loads(get_news_data)
        
        news_results = None
        
        if get_news_response["articles"]:
            
            news_results_list = get_news_response["articles"]
            
            news_results = process_results(news_results_list)
        
    return news_results


def process_results(news_list):
    
    """
    function that process results and return list of objexts
    
    """ 
    
    news_results = []
    
    for news_item in news_list:
        
        title = news_item.get("title")
        author = news_item.get("author")
        description = news_item.get("description")
        link = news_item.get("url")
        urlToImage = news_item.get("urlToImage")
        publishedAt = news_item.get("publishedAt")
        content = news_item.get("content")
        
        if title:
            news_object = Articles(author, title, description, link, urlToImage,publishedAt,content)
            news_results.append(news_object)
        
       
    return news_results 



def get_sources(category):
    
          

        
        
           
    
    