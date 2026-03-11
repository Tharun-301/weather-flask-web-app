# 🌤️ Weather Web App — Python Backend Project

A **Python Flask Weather Application** that fetches real-time weather data using the **OpenWeatherMap API** and displays it through a clean web interface.

This project demonstrates **backend development, API integration, and web deployment** using Python.

---

## 🚀 Live Demo

🌐 **Live Website:**https://weather-flask-web-app-2.onrender.com

---

## 📌 Project Overview

This application allows users to search for any city and view current weather conditions including:

* 🌡️ Temperature
* 🤔 Feels Like Temperature
* 💧 Humidity
* 🌬️ Wind Speed
* ☁️ Weather Condition
* 🌤️ Dynamic Weather Icons

The backend communicates with a weather API and renders data using HTML templates.

---

## 🛠️ Tech Stack

### Backend

* Python
* Flask
* Requests
* Gunicorn (Production Server)
* python-dotenv

### Frontend

* HTML5
* CSS3
* Jinja2 Templates

### API

* OpenWeatherMap API

### Deployment

* Render (Cloud Hosting)

---

## ⚙️ Installation (Run Locally)

### 1️⃣ Clone Repository

```
git clone https://github.com/Tharun-301/weather-flask-web-app.git
cd weather-app
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
```

Activate:

**Windows**

```
venv\Scripts\activate
```

**Mac/Linux**

```
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Add Environment Variables

Create `.env` file:

```
API_KEY=8d2796e1788bc20b9466f2c0f9eb4e5c
```

Get API key from:
https://openweathermap.org/api

---

### 5️⃣ Run Application

```
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

## 🌐 Deployment (Render)

1. Push project to GitHub
2. Create **Web Service** on Render
3. Set:

```
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app
```

4. Add Environment Variable:

```
API_KEY= your_api_key
```

Deploy 🚀

---

## ✨ Features

✅ Python Backend Architecture
✅ REST API Integration
✅ Secure Environment Variables
✅ Dynamic Weather Icons
✅ Responsive UI
✅ Error Handling (City Not Found)
✅ Cloud Deployment Ready

---

## 🧠 What I Learned

* Building backend applications using Flask
* Consuming third-party APIs
* Template rendering with Jinja2
* Environment variable management
* Production deployment using Gunicorn
* Cloud hosting with Render

---

## 🔮 Future Improvements

* 🌙 Dark/Light Mode
* 📍 Auto Location Detection
* 📅 5-Day Forecast
* 📱 Mobile Optimization
* 🔄 Background changes based on weather

---

## 👨‍💻 Author

**Tharun Sathunuru**

* GitHub: https://github.com/Tharun-301
* LinkedIn: *(Add your LinkedIn profile)*

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
