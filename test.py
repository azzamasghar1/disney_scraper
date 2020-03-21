import os
import time

import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

print('lets get started')

""" Load chrome driver """
directory = os.getcwd()
if os.name == 'posix':
    chromeDriver = directory + '/chromedriver'
else:
    chromeDriver = directory + '/chromedriver.exe'


""" Web Driver Configurations """
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument('--ignore-certificate-errors')
options.add_argument("window-size=1920,1080")
driver = webdriver.Chrome(executable_path=chromeDriver, options=options)
actions = ActionChains(driver)

""" Starting Url """
email = 'azzam.asghar@interstellus.com'
password = 'ZuCvvD2bhzbT'
url = 'https://www.disneyplus.com/login'
driver.get(url)

"""A method for scrolling the page."""
def scroll_bottom():
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(20)
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break

        last_height = new_height

""" Enter Email in the field and submit """
try:
    print('Entering Email.')
    email_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, 'email')))
    email_field.send_keys(email)
    driver.find_element_by_name("dssLoginSubmit").click()
    print('Entering Email Done.\n')

except Exception as e:
    print(e)
    pass

""" Enter Password in the field and submit """
try:
    print('Entering Password.')
    password_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, 'password')))
    password_field.send_keys(password)
    driver.find_element_by_name("dssLoginSubmit").click()
    print('Entering Password done.\n')

except Exception as e:
    print(e)
    pass

""" Wait for home page to load and extract data """
try:
    print('Waiting for Home Div.')
    WebDriverWait(driver, 40).until(
        EC.presence_of_element_located((By.ID, 'home-collection')))
    print('Found Home Div.\n')
    
    scroll_bottom()
    print('Scrolled to bottom.\n')

    print('Horizentally Scroll lists.\n')
    slick_tracks = driver.find_elements_by_css_selector('div.slick-track')
    for idx, slick_track in enumerate(slick_tracks):
        print(slick_track)
        print('console.log(document.getElementsByClassName("slick-track"));document.getElementsByClassName("slick-track")[0].style.transform = "translate3d(-' + str(slick_track.size['width']) + 'px, 0px, 0px)"')
        driver.execute_script(
            'console.log(document.getElementsByClassName("slick-track"));document.getElementsByClassName("slick-track")[0].style.transform = "translate3d(-' + str(slick_track.size['width']) + 'px, 0px, 0px)"'
        )

except Exception as e:
    print(e)
    pass
