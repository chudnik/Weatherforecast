import requests
import json

city = 'Moscow'

url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'

weather_data = requests.get(url).json()

weather_data_structure = json.dumps(weather_data, indent=2)
print(weather_data_structure)
