from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
def search_and_go(loc, driver):
    ''''
    Melakukan pencarian kota berdasarkan input
    loc = input kota
    '''
    # Menentukan lokasi search box
    #search = driver.find_element_by_class_name('_1xq16jy')
    #search = driver.find_element_by_xpath("//input[@placeholder='Where are you going?']")
    time.sleep(5)
    search = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@placeholder='Where are you going?']")))
    #search = WebDriverWait(driver, 20).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "_1xq16jy")))

    #driver.find_element_by_class_name('_1xq16jy').click()
    driver.implicitly_wait(5)
    search.send_keys(loc)
    driver.implicitly_wait(10)
    time.sleep(3)
    #actions = ActionChains(driver)
    search.send_keys(Keys.TAB + Keys.TAB + Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER)
    # Send keys without element

    #search.send_keys(Keys.RETURN)
    #actions.send_keys(Keys.TAB)
    #time.sleep(5)
    #actions.send_keys(Keys.TAB)
    #time.sleep(5)
    #actions.send_keys(Keys.TAB)
    #time.sleep(5)
    #actions.send_keys(Keys.TAB)
    #time.sleep(5)
    #actions.send_keys(Keys.TAB)
    #time.sleep(5)
    #actions.send_keys(Keys.RETURN)

    #go = WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, '_1mzhry13'))).click()
    curr_url = driver.current_url
    return curr_url


    # find
    #go = driver.find_element_by_class_name('_m9v25n')
    #return go.click()





