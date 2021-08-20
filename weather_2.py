import sys
import time
import requests
import datetime
import json


class WeatherForecast:
    def __init__(self, key, weatherdate):
        self.key = key
        self.newdata = {}
        self.weatherdate = weatherdate
        self.run()

    def get_api_data(self):
        url = "https://community-open-weather-map.p.rapidapi.com/forecast/daily"

        querystring = {"q": "Warszawa", "lat": "35", "lon": "139", "cnt": "16", "units": "metric or imperial"}

        headers = {
            'x-rapidapi-key': self.key,
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        rowdata = response.json()
        return rowdata

    def dict_save(self, rowdata):
        for data in rowdata["list"]:
            dt = data["dt"]
            weather = data["weather"][0]["main"]
            self.newdata[dt] = weather

    def validate(self):
        difference = datetime.datetime.strptime(self.weatherdate, "%Y-%m-%d").date() - datetime.datetime.today().date()
        if difference.days > 16 or difference.days < 0:
            print("Date outside the range.")
            raise
        else:
            print("The weather forecast will be checked.")

    def file_save(self, data):
        with open("weather.json", "a", newline="") as file:
            file.write(json.dumps(data))

    def summary(self):
        start = datetime.datetime.strptime(self.weatherdate, "%Y-%m-%d")
        start_date = time.mktime(start.timetuple())
        end = start + datetime.timedelta(days=1)
        end_date = time.mktime(end.timetuple())
        for k, v in self.newdata.items():
            if k > start_date and k < end_date:
                if v == "Rain":
                    print("It will rain.")
                if v == "Clouds":
                    print("I don't know (if it will rain).")
                if v == "Clear":
                    print("It won't rain.")

    def run(self):
        self.validate()
        data = self.get_api_data()
        self.dict_save(data)
        self.file_save(data)
        self.summary()

key = sys.argv[1]
weatherdate = sys.argv[2]
wf = WeatherForecast(key, weatherdate)
