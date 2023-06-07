import requests
import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
EXERCISE_ENDPOINT = os.environ.get("EXERCISE_ENDPOINT")
UPDATE_ENDPOINT = os.environ.get("UPDATE_ENDPOINT")
BEARER_AUTHENTICATION = os.environ.get("BEARER_AUTHENTICATION")

# Press the green button in the gutter to run the script.

exercise_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_parameters = {
    "query": input("Tell me which exercise you did: "),
    "gender": "male",
    "weight_kg": 75,
    "height_cm": 173,
    "age": 30
}

response = requests.post(url=EXERCISE_ENDPOINT, headers=exercise_headers, json=exercise_parameters)
response.raise_for_status()
data = response.json()
exercises_data = data["exercises"][0]
exercise = exercises_data["user_input"]
duration = exercises_data["duration_min"]
calories = exercises_data["nf_calories"]

date = dt.datetime.now()
date_now = date.strftime("%d/%m/%Y")
time_now = date.strftime("%X")

update_json = {
    "workout": {
        "date": date_now,
        "time": time_now,
        "exercise": str(exercise).title(),
        "duration": str(duration).title(),
        "calories": str(calories).title(),
    }
}

data = {"ip": "1.1.2.3"}
headers = {
    "Authorization": BEARER_AUTHENTICATION
}

update_response = requests.post(url=UPDATE_ENDPOINT, json=update_json, headers=headers)
update_response.raise_for_status()
print(update_response.text)
