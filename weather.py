import sys
import requests
import datetime

key = sys.argv[1]
weatherdate = sys.argv[2]
newdata = {}


def api_data_downloading():
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
    return newdata


def proper_day():
    difference = datetime.datetime.strptime(sys.argv[2], "%Y-%m-%d").date() - datetime.datetime.today().date()
    if difference.days > 16 or difference.days < 0:
        print("Date outside the range.")
        pass
    else:
        print("The weather forecast will be checked.")


def weather_check():
    if weatherdate in newdata == "Rain":
        print("It will rain.")
    if weatherdate in newdata == "Clouds":
        print("I don't know (if it will rain).")
    if weatherdate in newdata == "Clear":
        print("It won't rain.")


print(proper_day())
print(api_data_downloading())
print(weather_check())
