from flask import Flask , render_template , request
from weather import get_weather_detailes
from waitress import serve

app=Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city=request.args.get('city')
    if not  bool(city.strip()):
        city="Mysore"
    weather_data=get_weather_detailes(city)

    # if the city is not found by the API
    if not  weather_data['cod'] == 200:
        return  render_template(
            "citynotfound.html",
            title=city,
        )
    return render_template (
        "weather.html",
        title=weather_data['name'],
        status=weather_data['weather'][0]['description'].capitalize(),
        temp=f"{weather_data['main']['temp']:.2f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}",
    )

if __name__=="__main__":
    serve(app, host="0.0.0.0", port=8080)