from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from decouple import config
import time

APARTMENTS_FORM = config("APARTMENTS_HREF")


all_data = requests.get("https://appbrewery.github.io/Zillow-Clone/")
almost_soup = all_data.text
soup = BeautifulSoup(almost_soup, "html.parser")

classifieds = soup.find_all(
    "span", class_="PropertyCardWrapper__StyledPriceLine")

# Get Adresses:
whole_adresses = soup.select("address[data-test='property-card-addr']")
dirty_addresses = [adress.get_text().strip() for adress in whole_adresses]

cleaned_addresses = []
for address in dirty_addresses:
    if " | " in address:
        cleaned_addresses.append(address.split(" | ")[1])
    else:
        cleaned_addresses.append(address)

# Get Prices:
all_prices = [apartment.get_text() for apartment in classifieds]
allowed_chars = [",", "$", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
cleaned_prices = []
for price in all_prices:
    cleaned_prices.append(
        "".join(char for char in price if char in allowed_chars))


# Get Hiperlinks:
whole_links = soup.find_all("a", class_="StyledPropertyCardDataArea-anchor")
links = [link.attrs["href"] for link in whole_links]


# Combining addresses, prices and links:
address_price_link = list(zip(cleaned_addresses, cleaned_prices, links))

# Filling in Google forms:


lists_len = len(address_price_link)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(url=APARTMENTS_FORM)

for n in range(lists_len):
    time.sleep(3)
    answer_fields = driver.find_elements(By.CSS_SELECTOR, ".whsOnd.zHQkBf")
    send_button = driver.find_element(
        By.CSS_SELECTOR, "span.l4V7wb.Fxmcue > span.NPEfkd.RveJvd.snByac")
    idx = 0
    for item in answer_fields:
        item.send_keys(address_price_link[n][idx])
        idx += 1
    send_button.click()
    time.sleep(3)

    new_answer_link = driver.find_element(By.CSS_SELECTOR, "a")
    new_answer_link.click()
