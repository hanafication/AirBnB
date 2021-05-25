import requests
from bs4 import BeautifulSoup

class pageScrape:
    # Constructor
    def __init__(self, driver):
        self.driver = driver


   # get listings
    def scrape_single_element(self):
        ''''
        Get listings from search url
        curr_url = current page url
        '''
        # Getting page source/html
        driver = self.driver
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Getting single listings element
        #listing = soup.find_all('div', '_gig1e7')
        return print(soup.prettify())


