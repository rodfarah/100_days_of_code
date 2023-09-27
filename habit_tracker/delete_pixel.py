from decouple import config
import requests as rq

GRAPH_NAME = "graph01"
PIXELA_TOKEN = config("PIXELA_TOKEN")
PIXELA_USERNAME = config("PIXELA_USERNAME")

delete_day = "20230925"

user_token = {
    "X-USER-TOKEN" : PIXELA_TOKEN
}

DELETE_ENDPOINT = f"https://pixe.la/v1/users/{PIXELA_USERNAME}/graphs/{GRAPH_NAME}/{delete_day}"

delete_request = rq.delete(url=DELETE_ENDPOINT, headers=user_token)

print(delete_request.text)