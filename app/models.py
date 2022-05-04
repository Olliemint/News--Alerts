class Articles:
    
    def __init__(self,title,author,description,link,urlToImage,publishedAt,content):
        
        self.title = title
        self.author = author
        self.description = description
        self.link = link
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content


class Source:
    """
    source class to define source objects
    """
    
    def __init__(self,name,description,url):
        
        self.name = name
        self.description = description
        self.url = url    