from scraper.scraper import scraper
from search.search import search_and_go, iterating_pages
from to_pandas import to_csv,to_pandas

while True:
    print('Menu')
    print('1. Scrape City')
    print('2. Exit\n')
    menu = input('Choose a menu:')

    if menu == str(1):
        loc = input('Please input city: ')
        driver = scraper()
        # search = driver.find_element_by_class_name('_1xq16jy').click()
        curr_url = search_and_go(loc=loc, driver=driver)

        test_pages = iterating_pages(driver=driver, loc=loc)
        print(test_pages)
        test_scrape = to_csv(loc=loc, dataframe=to_pandas(test_pages))
    elif menu == str(2):
        exit()
    else:
        print('I know you wanna go home')
        exit()

# driver.close()


# if __name__ == '__main__':
#    scraper()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
