class NewsSource:
    '''
    class that defines news objects
    '''
    def __init__(self,id,name,description,url,category,language,country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country
               
class Articles:
    '''
    class that defines articles objects
    ''' 
    author = ""
    title = ""
    description = ""
    url = ""
    urlToImage = ""
    publishedAt = ""
    content = ""
    id=""
    def __init__(self,author,title,description,url,urlToImage,publishedAt,content,id):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
        self.id = id