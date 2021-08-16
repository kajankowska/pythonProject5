import sys
import requests
import datetime

key = sys.argv[1]
weatherdate = sys.argv[2]


class Forecast:
    def __init__(self, day, city):
        self.day = datetime.datetime.strptime(sys.argv[2], "%Y-%m-%d").date()
        self.city = city

    def proper_day(self):
        difference = self.day - datetime.datetime.today().date()
        if difference.days > 16:
            return False
        if difference.days < 0:
            return False
        return True


def api_data_downloading():
    url = "https://community-open-weather-map.p.rapidapi.com/forecast/daily"

    querystring = {"q": "Warszawa", "lat": "Warszawa", "lon": "Warszawa", "cnt": "16", "units": "metric or imperial"}

    headers = {
        'x-rapidapi-key': key,
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    rowdata = response.json()
    newdata = {}

    for data in rowdata["list"]:
        dt = data["dt"]
        print(dt)
        weather = data["weather"][0]["main"]
        print(weather)
        newdata[dt] = weather
    return newdata


print(api_data_downloading())
