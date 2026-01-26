from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://karineminasian.tilda.ws")
time.sleep(3)
driver.quit()