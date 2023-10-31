from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.types

SIGN_UP_FORM_URL = "https://web.archive.org/web/20220120120408/http://secure-retreat-92358.herokuapp.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(url=SIGN_UP_FORM_URL)

first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
button = driver.find_element(By.CSS_SELECTOR, value="button")

first_name.click()
first_name.send_keys("Rod")
last_name.send_keys("Far")
email.send_keys("teste@testando.com")
button.click()
