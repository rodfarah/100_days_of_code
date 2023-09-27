import requests as rq
from decouple import config

GRAPH_NAME = "graph01"
PIXELA_TOKEN = config("PIXELA_TOKEN")
PIXELA_USERNAME = config("PIXELA_USERNAME")

edit_day = "20230925"
liters = "3"


edit_params = {
    "quantity" : liters
}

user_token = {
    "X-USER-TOKEN" : PIXELA_TOKEN
}


UPDATE_ENDPOINT = f"https://pixe.la/v1/users/{PIXELA_USERNAME}/graphs/{GRAPH_NAME}/{edit_day}"

update_request = rq.put(url=UPDATE_ENDPOINT, json=edit_params, headers=user_token)

print(update_request.text)