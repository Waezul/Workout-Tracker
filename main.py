import requests
import os
from datetime import datetime


APP_ID = os.environ.get("app_id")
API_KEY = os.environ.get("app_key")


host_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

YOUR_TOKEN= os.environ.get("MY_TOKEN")

query = input("What excercises have you done today and for how long? ")

config = {
    "query": query
}
username = "41e9b38c1b75f2544c312c6e79521493"
project = "myWorkouts"
file = "workouts"

sheety_endpoint = f"https://api.sheety.co/{username}/{project}/{file}"

print(APP_ID)
print(API_KEY)
print(YOUR_TOKEN)


response= requests.post(url=host_endpoint,json=config,headers=headers)
data= response.json()
print(data)

today = datetime.now()
date = (today.strftime("%Y-%m-%d"))
current_time = today.strftime("%H:%M:%S")
print(date)

for exercise in data['exercises']:
    exercise_name = exercise['user_input']
    duration = exercise['duration_min']
    calories = exercise['nf_calories']

    print(f"Exercise: {exercise_name}")
    print(f"Duration: {duration} minutes")
    posting = {
        "workout" : {
            "date": date,
            "time": current_time,
            "exercise": exercise_name,
            "duration": duration,
            "calories": calories
        }
    }

    # rows_response = requests.post(url=sheety_endpoint,json=posting)

    bearer_headers = {
        "Authorization": f"Bearer {YOUR_TOKEN}"
    }
    sheet_response = requests.post(
        url=sheety_endpoint,
        json=posting,
        headers=bearer_headers
    )
    print(sheet_response.text)