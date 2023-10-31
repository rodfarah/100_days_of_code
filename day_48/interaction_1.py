from selenium import webdriver
from selenium.webdriver.common.by import By

WIKIPEDIA_URL = "https://en.wikipedia.org/wiki/Main_Page"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(url=WIKIPEDIA_URL)

article_counter = driver.find_element(By.CSS_SELECTOR, "#articlecount a")

print(article_counter.text)

driver.quit()