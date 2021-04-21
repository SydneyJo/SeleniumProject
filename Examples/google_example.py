from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\seleniumdrivers\chromedriver.exe")
driver.get("http://www.google.com")

search_input = driver.find_element_by_xpath('//input[@title="검색"]')
search_input.send_keys("selenium chrome driver download ")
search_input.send_keys(Keys.ENTER)
sleep(10)
driver.close()

