import requests
from datetime import datetime

GENDER = "MALE"
WEIGHT_KG = "90"
HEIGHT = "180.2"
AGE = "19"

APP_ID = "3f171b53"
API_KEY = "2c108a15e0e4218aeb50d3bb73e5281f"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/cc76a3bcc7fa121b2814766b6bac381b/myWorkouts/workouts"

now = datetime.now()
exercise_input = input("Tell which exercise you did today?: ")

header = {
    "x-app-id": APP_ID,
    'x-app-key': API_KEY
}

parameters = {
    'query': exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=header)
response.raise_for_status()
result = response.json()
sheet_post = {
    "workout":
        {
            "date": now.strftime("%d/%m/%Y"),
            "time": now.strftime("%I:%M %p"),
            "exercise": result['exercises'][0]['name'],
            "duration": int(result['exercises'][0]['duration_min']),
            "calories": result['exercises'][0]['nf_calories'],
        }
}
print(sheet_post)
sheet_response = requests.post(url="https://api.sheety.co/cc76a3bcc7fa121b2814766b6bac381b/myWorkouts/workouts", json=sheet_post)

