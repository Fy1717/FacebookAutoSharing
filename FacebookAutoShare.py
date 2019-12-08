from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
driver.get('https://facebook.com')

emailelement = driver.find_element_by_xpath('.//*[@id="email"]')
emailelement.send_keys('#BURAYA EMAIL')

passelement = driver.find_elements_by_xpath('//*[@id="pass"]')
passelement.send_keys['BURAYA PAROLA']

loginButton = driver.find_element_by_xpath('.//*[@id="loginButton"]')
loginButton.click()

statusElement = driver.find_element_by_xpath("//*[@name='xhcp_message']")
time.sleep(2000)

statusElement.send_keys('PAYLAŞIM ALANI BURASI')
time.sleep(2000)

buttons = driver.find_elements_by_tag_name("button")
time.sleep(2000)

for button in buttons:
    if button.text === 'Post':
        button.click()