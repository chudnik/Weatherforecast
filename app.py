from flask import Flask, render_template
import requests
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    city = 'Moscow'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'

    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()

        temperature = weather_data['main']['temp']
        temperature_feels = weather_data['main']['feels_like']
        wind_speed = weather_data['wind']['speed']
        sunrise = weather_data['sys']['sunrise']
        sunset = weather_data['sys']['sunset']
        cloudiness = weather_data['clouds']['all']
        coord_lon = weather_data['coord']['lon']
        coord_lat = weather_data['coord']['lat']

        sunrise_time = datetime.fromtimestamp(sunrise).strftime('%H:%M:%S')
        sunset_time = datetime.fromtimestamp(sunset).strftime('%H:%M:%S')

        return render_template('index.html', city=city, temperature=temperature, temperature_feels=temperature_feels,
                               wind_speed=wind_speed, sunrise_time=sunrise_time, sunset_time=sunset_time,
                               cloudiness=cloudiness, coord_lon=coord_lon, coord_lat=coord_lat)

    except requests.exceptions.HTTPError as errh:
        return render_template('index.html', error=f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        return render_template('index.html', error=f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        return render_template('index.html', error=f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        return render_template('index.html', error=f"Error: {err}")
    except KeyError as ke:
        return render_template('index.html', error=f"Key Error: {ke}")

if __name__ == '__main__':
    app.run(debug=True)