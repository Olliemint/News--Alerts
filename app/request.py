

from textwrap import indent
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



def get_sources():
    
    get_sources_url = source_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        
        get_sources_response = json.loads(get_sources_data)
        
        source_results = None
        if get_sources_response['sources']:
            
            source_results_list = get_sources_response['sources']
            source_results = process_sources(source_results_list)
    
    return source_results        

def process_sources(source_list):
    """
    function transform to list objects
    
    """  
    
    source_results = []
    for source_item in source_list:
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        
        if name:
            source_object = Source(name,description,url)
            source_results.append(source_object)
    
    return source_results        
        
        
              
          

        
        
           
    
    