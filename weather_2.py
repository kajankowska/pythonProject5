import sys
import time
import requests
import datetime


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

    def edit_file(self):
        with open("forecast.txt", "a") as file:
            file.write(f"{weatherdate}\n")

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

    def file_summary(self):
        f = open("forecast.txt", "r")
        for weatherdate in f:
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
            return weatherdate

    def api_summary(self):
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
        self.edit_file()
        self.dict_save(data)
        self.file_summary()
        self.api_summary()
        self.__iter__()
        self.__getitem__()

    def __getitem__(self):
        self.weatherdate = datetime.datetime.strptime(weatherdate, "%Y-%m-%d").date()
        pass

    def __iter__(self):  # iterator returning all dates the weather is known
        for k in self.newdata.keys():
            k = datetime.datetime.fromtimestamp(int(k)).strftime("%Y-%m-%d")
            print(k)
        return iter(self.newdata)


key = sys.argv[1]

if len(sys.argv) < 3:  # if the date is not specified, the next day is selected
    d = datetime.datetime.today().date()
    date = d + datetime.timedelta(days=1)
    weatherdate = str(date)
else:
    weatherdate = sys.argv[2]


wf_date = WeatherForecast(key, weatherdate)  # answer about the weather for the given date (weatherdate)
wf.items() =  # tuple generator for retained results when calling
