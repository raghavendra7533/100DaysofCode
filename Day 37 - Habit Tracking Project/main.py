import requests
from datetime import datetime


today = datetime.now()
today_strf = today.strftime("%Y%m%d")

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_USERNAME = "raghav7533"
PIXELA_TOKEN = "j3asn5ab6ca8kjs0349nla"
PIXELA_USER_CREATION_PARAMS = {
    "token": "j3asn5ab6ca8kjs0349nla",
    "username": "raghav7533",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
PIXELA_GRAPH_CREATION_PARAMS = {
    "id": "graph1",
    "name": "100 days of code Graph",
    "unit": "days",
    "type": "int",
    "color": "kuro"
}
PIXELA_HEADER = {
    "X-USER-TOKEN": PIXELA_TOKEN
}
PIXELA_GRAPH_ID = "graph1"
PIXELA_PIXEL_CREATION_DATA = {
    "date": today_strf,
    "quantity": "1",
}

# Creating a user
# response = requests.post(url=PIXELA_ENDPOINT, json=PIXELA_USER_CREATION_PARAMS)
# print(response.text)

# Creating a graph definition
# graph_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs"
# response = requests.post(url=graph_endpoint, json=PIXELA_GRAPH_CREATION_PARAMS, headers=PIXELA_HEADER)

# Creating a pixel
# pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}"
# response = requests.post(url=pixel_creation_endpoint, json=PIXELA_PIXEL_CREATION_DATA, headers=PIXELA_HEADER)
# print(response.json())

# Deleting a graph
update_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}/{today_strf}"
new_pixela_data = {
    "quantity": "1",
}
request = requests.put(url=update_endpoint, json=new_pixela_data, headers=PIXELA_HEADER)
