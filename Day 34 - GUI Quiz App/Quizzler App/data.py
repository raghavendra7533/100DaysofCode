import requests

"""CONSTANTS"""
PARAMETERS = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php", params=PARAMETERS)
data = response.json()
question_data = data['results']
