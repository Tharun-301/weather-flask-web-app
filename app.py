from flask import Flask, render_template, request
from weather import get_current_weather
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Weather route
@app.route("/weather")
def weather():
    city = request.args.get("city")

    if not city:
        return render_template("index.html")

    weather_data = get_current_weather(city)

    # City not found
    if not weather_data:
        return render_template("city-not-found.html")

    # Extract data for template
    title = weather_data["name"]
    status = weather_data["weather"][0]["description"].title()
    temp = weather_data["main"]["temp"]
    feels_like = weather_data["main"]["feels_like"]

    humidity = weather_data["main"]["humidity"]
    wind_speed = weather_data["wind"]["speed"]
    icon = weather_data["weather"][0]["icon"]

    return render_template(
        "weather.html",
        title=title,
        status=status,
        temp=temp,
        feels_like=feels_like,
        humidity=humidity,
        wind_speed=wind_speed,
        icon=icon
    )


if __name__ == "__main__":
    app.run(debug=True)