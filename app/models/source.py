class Source:
    '''
    Sources class to define article Objects
    '''

    def __init__(self,id,name,description,url,category,country,language):
        self.id =id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster
        self.country = country
        self.language = language