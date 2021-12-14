import os
class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL ='https://newsapi.org/v2/top-headlines/sources?apiKey={}'
    ARTICLES_API_BASE_URL = 'https://newsapi.org/v2/everything?q={}&sortBy=popularity&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
class prodConfig(Config):
    '''
    Production Configuration Child Class
    '''
    '''
    Args:
        Config:It inherits from the parent configuration class with the general configurations
    '''
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
class DevConfig(Config):
    '''
    Development Configuration Child Class
    Args:
        Config:It inherits from the parent configuration class with the general configurations
    '''
    DEBUG = True
config_options = {
    'development':DevConfig,
    'production':prodConfig
}