import requests
from datetime import datetime

date = datetime.today().strftime('%d/%m/%Y')
time = datetime.today().strftime('%H:%M:%S')


nutrionx_api_appid = 'd11c9bfa'
nutrionx_api_key = '42a485e8fcb3ab777e9756b37ad80f3d'
BASEURL = 'https://trackapi.nutritionix.com/v2/natural/exercise'
url_headers = {
    "Content-Type": "application/json",
    "x-app-id": nutrionx_api_appid, 
    "x-app-key": nutrionx_api_key
}
body = input('Tell me which exercises you did: ')

json_data = {
    "query": body
}

nutrionx_request = requests.post(url=BASEURL, headers=url_headers, json=json_data)
nutrionx_request.raise_for_status()
raw_workout_data = nutrionx_request.json()['exercises']

workout_data = [{'date':date, 'time':time, 'name':data.get('name') , 'duration':data.get('duration_min'), 'calories':data.get('nf_calories')} for data in raw_workout_data]

for exercise in workout_data:
    sheet_inputs = {
        "workout": {
            "date": exercise['date'],
            "time": exercise['time'],
            "exercise": exercise['name'],
            "duration": exercise['duration'],
            "calories": exercise['calories'],
        }
    }
    
    #name = exercise['name'].strip()
    sheet_request = requests.post(url='https://api.sheety.co/915a586c4846791d93893a0e68ad6c52/myWorkouts/workouts', json=sheet_inputs)
    sheet_request.raise_for_status()
    sheet_request.text()