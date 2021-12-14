import unittest
from app.models import NewsSource

class NewsSourceTest(unittest.TestCase):
    '''
    Test Class to test the behavior of the News_source Class
    '''
    def setUp(self):
        '''
        setup method that runs before every test
        '''
        self.new_source = NewsSource("abc-news","ABC News","Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.","https://abcnews.go.com","general","en","au")
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,NewsSource))