from flask import Flask, render_template, request
from weather import get_current_weather
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Weather Page
@app.route("/weather")
def weather():
    city = request.args.get("city", "").strip()

    if not city:
        return render_template("index.html")

    weather_data = get_current_weather(city)

    if not weather_data:
        return render_template("city-not-found.html")

    try:
        return render_template(
            "weather.html",
            title=weather_data["name"],
           status = weather_data["weather"][0]["main"].lower(),
            temp=weather_data["main"]["temp"],
            feels_like=weather_data["main"]["feels_like"],
            humidity=weather_data["main"]["humidity"],
            wind_speed=weather_data["wind"]["speed"],
            icon=weather_data["weather"][0]["icon"]
        )
    except KeyError:
        return render_template("city-not-found.html")


if __name__ == "__main__":
    app.run(debug=True)