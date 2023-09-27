import requests as rq
from decouple import config
from datetime import datetime, timedelta

GRAPH_NAME = "graph01"


PIXELA_TOKEN = config("PIXELA_TOKEN")
PIXELA_USERNAME = config("PIXELA_USERNAME")
base_date = datetime.today()
date = (base_date - timedelta(1)).strftime("%Y%m%d")


PIXEL_ENDPOINT = f"https://pixe.la/v1/users/{PIXELA_USERNAME}/graphs/{GRAPH_NAME}"

pixel_params = {
    "date" : date,
    "quantity" : "2"
}

other_params = {
    "X-USER-TOKEN" : PIXELA_TOKEN
}

pixel_request = rq.post(url=PIXEL_ENDPOINT, json=pixel_params, headers=other_params)

print(pixel_request.text)