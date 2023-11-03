from selenium import webdriver
from selenium.webdriver.common.by import By
GAME_URL = "http://orteil.dashnet.org/experiments/cookie/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(url=GAME_URL)


# --------------- COLECTING DATA -----------------------


def get_score() -> int:
    """ Return cookies actual score"""
    return int(driver.find_element(By.ID, "money").text.replace(",", ""))


def cookies_per_second() -> str:
    """ Colect the respective element and print as text"""
    return driver.find_element(By.ID, "cps").text


class Cookie:
    def __init__(self) -> None:
        self.cookie_element = driver.find_element(By.ID, "cookie")

    def click_on_cookie(self):
        self.cookie_element.click()


class Store:
    def __init__(self) -> None:
        # Finding Store Elements (all <div>):
        self.general_elements = driver.find_elements(
            By.CSS_SELECTOR, "#store div")
        # Getting element's IDs:
        self.ids = [element.get_attribute("id")
                    for element in self.general_elements]

    def generate_dict_click_element(self, score):
        # Getting each element, from most expensive to cheapest:
        self.elements_list = [driver.find_element(
            By.ID, f"{id}") for id in self.ids][7::-1]
        # Getting name and cost of each element:
        self.element_contents = [element.text.splitlines()[0]
                                 for element in self.elements_list]
        self.element_costs = [int(element.split(" - ")[1].replace(",", ""))
                              for element in self.element_contents]
        # Generating a dict (keys = costs, values = elements)
        self.brain_dict = {cost: element for cost, element in (
            zip(self.element_costs, self.elements_list))}
        # Click on an element (value), acording to a given score (function parameter)
        for cost, element in self.brain_dict.items():
            if cost <= score:
                element.click()
                break

    def click_on_item(self, item):
        item.click()

