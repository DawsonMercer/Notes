import requests
import json
from pprint import pprint

def main():
    city_name = input("Enter the name of a city to get the current weather: ")


    data = current_weather.json()
    temp = data['main']['temp']
    wind = data['wind']['speed']
    description = data['weather'][0]['description']
    print(f"Temperature in {city_name}: {temp}C")
    print(f"Wind speed in {city_name}: {wind}m/s")
    print(f"Weather description: {description}")

    # forecast = requests.get(f'http://pro.openweathermap.org/data/2.5/forecast/hourly?q={city_name}&appid=9a89ae19bbafaa755ee77f42433b487e')
    # data = forecast.json()
    # print(data)



if __name__ == "__main__":
    main()
