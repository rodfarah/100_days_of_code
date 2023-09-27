import requests as rq
from decouple import config

PIXELA_USERNAME = config("PIXELA_USERNAME")
PIXELA_TOKEN = config("PIXELA_TOKEN")
PIXELA_GRAPH_ENDPOINT = f"https://pixe.la/v1/users/{PIXELA_USERNAME}/graphs"
GRAPH_NAME = "graph01"


request_body = {
    "id": GRAPH_NAME,
    "name": "water_consumption",
    "unit": "liter",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}


graph_response = rq.post(url=PIXELA_GRAPH_ENDPOINT, json=request_body, headers=headers)

print(graph_response.text)
