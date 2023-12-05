import requests

API_KEY = "d3e4d99fa879cf74cfd463df7a1a725c"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = F"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    print("Weather in", city, "is", weather)
    print("Temperature is: ", round(temperature - 273.15, 2), "celsius")
else:
    print("An error occurred.")

