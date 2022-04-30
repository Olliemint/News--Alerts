from distutils.debug import DEBUG


class Config:
    
    news_base_url = "https://newsapi.org/v2/everything?q=Apple&from=2022-04-30&sortBy=popularity&apiKey={}"
    
    

class ProdConfig(Config):
    
    pass

class DevConfig(Config):
    
    pass
    DEBUG = True