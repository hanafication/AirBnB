import requests
from bs4 import BeautifulSoup

class pageScrape:

    # All information in elements of listings
    LISTING_INFORMATION = {'url': {'tag': 'a', 'get': 'href'},
                           'name': {'tag': 'span',  'class' : '_1whrsux9'},
                           'superhost': {'tag': 'div', 'class': '_ufoy4t'},
                           'desc': {'tag': 'div', 'class': '_b14dlit'},
                           'rooms': {'tag': 'div', 'class': '_kqh46o'},
                           'facilities': {'tag': 'div', 'class': '_kqh46o', 'order': 1},
                           'rating_reviews': {'tag': 'span', 'class': '_18khxk1'},
                           'price': {'tag': 'span', 'class': '_155sga30'}
                           }
    # Constructor
    def __init__(self, driver, curr_url):
        self.driver = driver
        self.curr_url = curr_url


    def using_selenium(self):
        ''''
        Get listings elements from search url
        using selenium
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
        ''''
        Get listings elements from searched url using requests
        '''
        soup = BeautifulSoup(requests.get(self.curr_url).content, 'html.parser')
        listings = soup.find_all('div', class_ = '_8s3ctt')
        print(len(listings))
        return listings

    def extract_single_listings(self, listings,loc):
        '''
        Extract all listings in single page
        '''

        listings_list = list()

        for listing in listings:
            listings_dict = dict()
            listings_dict['city'] = loc
            # Iterating for each information
            for info in pageScrape.LISTING_INFORMATION:
                try:
                    if 'class' in pageScrape.LISTING_INFORMATION[info]:
                        element = listing.find_all(pageScrape.LISTING_INFORMATION[info]['tag'], pageScrape.LISTING_INFORMATION[info]['class'])
                    elif 'span' in pageScrape.LISTING_INFORMATION[info]:
                        element = listing.find_all(pageScrape.LISTING_INFORMATION[info]['tag'], pageScrape.LISTING_INFORMATION[info]['span'])
                    else:
                        element = listing.find_all(pageScrape.LISTING_INFORMATION[info]['tag'])


                    # Element
                    orders = pageScrape.LISTING_INFORMATION[info].get('order', 0)
                    elements = element[orders]

                    # Values
                    if 'get' in pageScrape.LISTING_INFORMATION[info]:
                        output = elements.get(pageScrape.LISTING_INFORMATION[info]['get'])
                    else:
                        output = elements.get_text()

                    listings_dict[info] = output
                except:
                    listings_dict[info] = 'empty'


            listings_list.append(listings_dict)

        return listings_list






