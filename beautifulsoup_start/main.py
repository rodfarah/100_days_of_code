from bs4 import BeautifulSoup
import requests

all_data = requests.get("https://news.ycombinator.com/news")
almost_soup = all_data.text

soup = BeautifulSoup(almost_soup, "html.parser")
whole_line = soup.find(name="a", rel="noreferrer")
print(whole_line, "\n")
text_string = whole_line.get_text()
print(text_string, "\n")
article_link = whole_line.get("href")
print(article_link, "\n")

num_of_points = soup.find("span", class_="score").getText()
print(num_of_points)