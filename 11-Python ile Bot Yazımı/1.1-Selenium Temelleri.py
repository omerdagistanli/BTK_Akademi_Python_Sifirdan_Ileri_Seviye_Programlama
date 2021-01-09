from selenium import webdriver
import time

driver = webdriver.Firefox()

url = "http://github.com"

driver.get(url)

time.sleep(2)
driver.maximize_window()
driver.save_screenshot("github-screenshot.png")
print(driver.title)

time.sleep(2)
driver.close()
