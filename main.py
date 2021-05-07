from scraper.scraper import scraper
from search.search import search_and_go
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

loc = 'banyuwangi'
driver = scraper()
#search = driver.find_element_by_class_name('_1xq16jy').click()
search = search_and_go(loc = loc, driver = driver)
#search = search_and_go(driver = driver)


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    scraper()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
