import requests

# Указываем город
city = 'Moscow'

# Формируем запрос
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'

# Отправляем запрос на сервер и сразу получаем результат
weather_data = requests.get(url).json()

# Получаем данные о температуре и о том, как она ощущается
temperature = weather_data['main']['temp']
temperature_feels = weather_data['main']['feels_like']
wind_speed = weather_data['wind']['speed']
sunrise = weather_data['sys']['sunrise']
sunset = weather_data['sys']['sunset']
cloudiness = weather_data['clouds']['all']
coord_lon = weather_data['coord']['lon']
coord_lat = weather_data['coord']['lat']

# Преобразуем время рассвета и заката в читаемый формат
from datetime import datetime
sunrise_time = datetime.fromtimestamp(sunrise).strftime('%H:%M:%S')
sunset_time = datetime.fromtimestamp(sunset).strftime('%H:%M:%S')

# Выводим значения на экран
print(f'Сейчас в городе {city} {temperature} °C')
print(f'Ощущается как {temperature_feels} °C')
print(f'Скорость ветра {wind_speed} m/s')
print(f'Время рассвета {sunrise_time}')
print(f'Время заката {sunset_time}')
print(f'Облачность {cloudiness}%')
print(f'Координаты города {coord_lon}, {coord_lat}')
