# Day 37 - Habit Tracking Project
#### References
1. [[Status Codes]]
2. [[HTTP Request Methods]]

>[!info]- Advance Authentication and POST / PUT / DELETE Requests

## Sending a HTTP Request to the API for creating the user
- The api endpoint is [Pixe.la](https://pixe.la/v1/users)
- The request body has token, username, agreeTermsOfService and notMinor as `required`. 
- The request body also has a key `thanksCode` as optional.

## Setting up Pixela user
Use the requests library to post your params to create a user.
```python
import requests  
  
  
PIXELA_ENDPOINT = "https://pixe.la/v1/users"  
PIXELA_POST_PARAMS = {  
    "token": "j3asn5ab6ca8kjs0349nla",  
    "username": "raghav7533",  
    "agreeTermsOfService": "yes",  
    "notMinor": "yes"  
    }  
  
response = requests.post(url=PIXELA_ENDPOINT, json=PIXELA_POST_PARAMS)  
print(response.text)
```

```json output
{"message":"Success. Let's visit https://pixe.la/@raghav7533 , it is your profile page!",
 "isSuccess":true}
```

## Create a graph definition
### Params required
1. id
2. name
3. unit
4. type
5. color
### Headers required
1. Token

```python
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
  
#Creating a user  
response = requests.post(url=PIXELA_ENDPOINT, json=PIXELA_USER_CREATION_PARAMS)  
print(response.text)  
  
# Creating a graph definition  
graph_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs"  
response = requests.post(url=graph_endpoint, json=PIXELA_GRAPH_CREATION_PARAMS, headers=PIXELA_HEADER)
```

## Challenge 1 : POST a pixel
### Headers required
1. X-USER-TOKEN

### Params required
1. date
2. quantity

- Create two other constants for `graph id` and `pixel_creaation_data`
- Create a variable for the api endpoint
- Use the requests library to POST the request to the api
```python
PIXELA_GRAPH_ID = "graph1"  
PIXELA_PIXEL_CREATION_DATA = {  
    "date": "20231121",  
    "quantity": "1",  
}
pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}"  
response = requests.post(url=pixel_creation_endpoint, json=PIXELA_PIXEL_CREATION_DATA, headers=PIXELA_HEADER)  
print(response.json())
```

## Automate the date entry with `datetime` library
### Use `strftime` to format the date
```python
from datetime import datetime  

today = datetime.now()  
today_strf = today.strftime("%Y%m%d")

PIXELA_PIXEL_CREATION_DATA = {  
    "date": today_strf,  
    "quantity": "1",  
}
```
