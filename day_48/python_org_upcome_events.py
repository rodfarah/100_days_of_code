from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)


driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url="https://www.python.org/")

events = [event.text.split("\n") for event in driver.find_elements(By.CSS_SELECTOR, value=".event-widget li")]

result = {n : {"time": events[n][0], "name": events[n][1]} for n in range(len(events))}

driver.quit()
