# Day 38 - Workout Tracking Using Google Sheets
## Nutritionix API
#### References
- Check the API documentation for Nutritionix API, [link](https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/preview)

### Obtaining the API Keys and Authenticating
The API requires APP ID and APP KEY. The API also requires x-app-id, x-app-key and x-remote-user-id in the header

### Using the `/v2/natural/exercise` endpoint
Sending a post request to this endpoint with relevant header and body will trigger the LLM to generate the relevant json

## Sheety API Setup
#### References
- Check the API documentation for Sheety API, [Sheety API](https://sheety.co/docs)
Adding the sheety API endpoint to the code, `sheet_endpoint = "https://api.sheety.co/cc76a3bcc7fa121b2814766b6bac381b/myWorkouts/workouts"`
Using datetime module to fetch the date and time for the data entry in google sheets

## Full Code
```python
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
```
