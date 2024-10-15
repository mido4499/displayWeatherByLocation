from flask import Flask, render_template, request
import requests

app = Flask(__name__)
API_KEY = 'dac04569b7a50f271832ce79af7d025f'


@app.route('/')
def index():
    return render_template("index.html")



@app.route("/weatherbylocation")
def weatherByLocation():
    lat = request.args.get('lat')
    lon = request.args.get('lon')

    if lon and lat:
        url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={API_KEY}'
        response = requests.get(url)
        data = response.json()
        if data.get('cod') == 200:
            weather_info = {
                'city' : data['name'],
                'temperature' : data['main']['temp'],
                'description' : data['weather'][0]['description'],
                'humidity' : data['main']['humidity'],
                'wind_speed' : data['wind']['speed']
            }
        else:
            weather_info = {'error': 'location not found'}
    
    return render_template('weatherbylocation.html', weather_info = weather_info)


if __name__ == '__main__':
    app.run(debug=True)
