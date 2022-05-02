
class Config:
    
    BASE_URL = "https://newsapi.org/v2/everything?q=Apple&from=2022-05-02&sortBy=popularity&apiKey={}"
    SOURCE_URL = "https://newsapi.org/v2/top-headlines/sources?apiKey={}"
    

class ProdConfig(Config):
    
    pass

class DevConfig(Config):
    
    pass
    DEBUG = True