from bs4 import BeautifulSoup
import requests

# Getting data from Empire Website:
empire_html_data = requests.get(
    "https://www.empireonline.com/movies/features/best-movies-2/").text
film_soup = BeautifulSoup(empire_html_data, "html.parser")

descendant_tag_list = film_soup.find_all(
    "h3", class_="listicleItem_listicle-item__title__hW_Kn")

ascendant_film_list = [tag.getText() for tag in descendant_tag_list][::-1]

with open("/home/rofarah/Documents/TI/Code/100_days_of_code/beautifulsoup_start/top_100_movies/top_100_movies.txt", "w") as one_hundred_top_movies:
    for film in ascendant_film_list:
        one_hundred_top_movies.write(f"{film}\n")
