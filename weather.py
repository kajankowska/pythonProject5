import sys
import time
import requests
import datetime
import json

key = sys.argv[1]
weatherdate = sys.argv[2]
today = datetime.date.today()
unixdate = datetime.datetime.strptime(weatherdate, "%Y-%m-%d")
unixdate = time.mktime(unixdate.timetuple())

newdata = {}


with open("weather.json", "a") as file:
    file.write("")

    url = "https://community-open-weather-map.p.rapidapi.com/forecast/daily"

    querystring = {"q": "Warszawa", "lat": "35", "lon": "139", "cnt": "16", "units": "metric or imperial"}

    headers = {
        'x-rapidapi-key': key,
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    rowdata = response.json()

    for data in rowdata["list"]:
        dt = data["dt"]
        weather = data["weather"][0]["main"]
        newdata[dt] = weather


with open("weather.json", "a", newline="") as file:
    file.write(json.dumps(response.json()))


difference = datetime.datetime.strptime(sys.argv[2], "%Y-%m-%d").date() - datetime.datetime.today().date()
if difference.days > 16 or difference.days < 0:
    print("Date outside the range.")
else:
    print("The weather forecast will be checked.")


for k, v in newdata.items():
    if k >= unixdate:
        if k == "Rain":
            print("It will rain.")
        if k == "Clouds":
            print("I don't know (if it will rain).")
        if k == "Clear":
            print("It won't rain.")
