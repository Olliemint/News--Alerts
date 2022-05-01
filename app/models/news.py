class Articles:
    
    def __init__(self,title,author,description,content,link,image,publishedAt):
        
        self.title = title
        self.author = author
        self.description = description
        self.link = link
        self.image = image
        self.publishedAt = publishedAt
        self.content = content
    
    
class Sources:
    
    def __init__(self,id,name):
        
        self.name = name
        self.id = id
  
        
                   