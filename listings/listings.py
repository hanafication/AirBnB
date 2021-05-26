import requests
from bs4 import BeautifulSoup

class pageScrape:

    # All information in elements of listings
    LISTING_INFORMATION = {'url' : {'tag' : 'a', 'get' : 'href'},
                           'name' : {'tag' : 'a', 'get' : 'aria-label'},
                           'desc' : {'tag' : 'div', 'class' : '_b14dlit'}}
    # Constructor
    def __init__(self, driver, curr_url):
        self.driver = driver
        self.curr_url = curr_url

   # get listings
    def using_selenium(self):
        ''''
        Get listings from search url
        curr_url = current page url
        '''
        # Getting page source/html
        #driver = self.driver
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        #listings = soup.find_all('div', {'class' : '_8s3ctt'})
        # Getting single listings element
        #listing = soup.find_all('div', '_gig1e7')
        return soup

    # Get all elements with target information
    def using_requests(self):
        soup = BeautifulSoup(requests.get(self.curr_url).content, 'html.parser')
        listings = soup.find_all('div', class_ = '_8s3ctt')
        return listings

    # Get all elements from listings



