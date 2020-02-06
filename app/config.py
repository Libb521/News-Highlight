class Config:
    '''
    General configuration parent class
    '''

    NEWS_API_BASE_URL ='https://newsapi.org/v2/sources?apiKey=ec6dcb4967464bb0adb9cf6f91023edf'
    ARTICLES_BASE_URL ='https://newsapi.org/v2/everything?sources={}&apiKey=ec6dcb4967464bb0adb9cf6f91023edf'

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True