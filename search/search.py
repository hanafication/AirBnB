from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def search_and_go(loc, driver):
    ''''
    Melakukan pencarian kota berdasarkan input
    loc = input kota
    '''
    # Menentukan lokasi search box
    search = driver.find_element_by_class_name('_1xq16jy')
    #search = driver.find_element_by_xpath("//input[@placeholder='Where are you going?']").click()
    #search = WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH, "//input[@placeholder='Where are you going?']")))
    #search.clear()

    #search.send_keys(loc)
    return search




