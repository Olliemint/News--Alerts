import os
class Config:
    
    BASE_URL = "https://newsapi.org/v2/everything?q=Apple&from=2022-05-02&sortBy=popularity&apiKey={}"
    SOURCE_URL = "https://newsapi.org/v2/top-headlines/sources?apiKey={}"
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    
    pass

class DevConfig(Config):
    
    
    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}   