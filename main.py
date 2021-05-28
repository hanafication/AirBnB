from scraper.scraper import scraper
from search.search import search_and_go, iterating_pages

loc = 'jember'
driver = scraper()
# search = driver.find_element_by_class_name('_1xq16jy').click()
curr_url = search_and_go(loc=loc, driver=driver)

test_pages = iterating_pages(driver=driver)
print(len(test_pages))
print(test_pages)

# driver.close()


# if __name__ == '__main__':
#    scraper()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
