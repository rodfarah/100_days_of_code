from selenium import webdriver
from selenium.webdriver.common.by import By
import time
GAME_URL = "http://orteil.dashnet.org/experiments/cookie/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(url=GAME_URL)


# Finding cookie element in order to click on it
cookie = driver.find_element(By.ID, value="cookie")

# Finding store items (most expensive to cheapest)
time_machine_element = driver.find_element(By.CSS_SELECTOR, "[id = 'buyTime Machine']")
time_machine_cost = driver.find_element(By.CSS_SELECTOR, '[id = "buyTime machine"] b')

# TODO #1: Mapear todos os itens da loja de acordo com as duas linhas acima
# TODO #2: Criar dicionário em que o valor é key e o item da loja é o value; do valor mais caro para o mais barato
# TODO #3: a cada 5 segundos, fazer um loop no dicionário, comparando o valor de dinheiro disponível com o custo do \
# item mais caro.
# TODO #4: Nas verificações de cada 5 segundos, não interromper os cliques de cookies.



# cursor = driver.find_element(By.ID, value="buyCursor")
# cursor = driver.find_element(By.ID, value="buyCursor")
# cursor = driver.find_element(By.ID, value="buyCursor")
# cursor = driver.find_element(By.ID, value="buyCursor")
# cursor = driver.find_element(By.ID, value="buyCursor")
# cursor = driver.find_element(By.ID, value="buyCursor")
# cursor = driver.find_element(By.ID, value="buyCursor")

print(time_machine_cost.text)





# print(cursor.get_attribute("class"))



# first_time = time.time()

# while True:
#     cookie.click()
#     second_time = time.time()
#     if second_time - first_time > 5:
#         money = driver.find_element(By.ID,"money")
        