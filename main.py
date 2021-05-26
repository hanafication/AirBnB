from scraper.scraper import scraper
from search.search import search_and_go
from bs4 import BeautifulSoup
import requests
from listings.listings import pageScrape
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

loc = 'malang'
driver = scraper()
#search = driver.find_element_by_class_name('_1xq16jy').click()
curr_url = search_and_go(loc = loc, driver = driver)
# Scrape single listing
#soup = BeautifulSoup(driver.page_source, 'html.parser')
#print(soup.prettify())
# Getting single listings element
# listing = soup.find_all('div', '_gig1e7')

soup = pageScrape(driver=driver, curr_url=curr_url)
listings = soup.using_requests()
print(listings[0])
#driver.close()

#search = search_and_go(driver = driver)


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    scraper()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
