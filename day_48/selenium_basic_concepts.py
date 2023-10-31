from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://www.amazon.com/Toaster-Stainless-Digital-Function-Settings/dp/B0CC5SMLNT/ref=sr_1_6?crid=37OG3YX0JMEOI&keywords=toaster&qid=1698691265&sprefix=toaste%2Caps%2C226&sr=8-6&th=1")

price_dolar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

print(f"{price_dolar.text}.{price_cents.text}")

# driver.close() => closes one tab
driver.quit() # => closes all tabs (the whole browser)