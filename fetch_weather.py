import requests
import pandas as pd
import csv
import sqlite3
from datetime import datetime
import schedule
import time
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.environ.get('API_KEY')
CSV_FILE = 'weather_data.csv'

def fetch_weather_data(city):
    API_URL = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        weather_data = {
            'city': city,
            'timestamp': datetime.now().isoformat(),
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'cloud_cover': data['clouds']['all'],
            'wind_condition': data['wind']['speed'],
            'precipitation': bool(data.get('rain')),
            'remarks': data['weather'][0]['description'],
        }
        print("Fetched Data:", weather_data)
        save_to_csv(weather_data)
        insert_data_into_db(weather_data)
    else:
        print(f"Error fetching data for {city}: {response.status_code}, Response: {response.text}")

def setup_database():
    with sqlite3.connect('weather_data.db') as conn:
        cursor = conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS weather')
        cursor.execute('''
            CREATE TABLE weather (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT NOT NULL,
                timestamp TEXT NOT NULL,
                temperature REAL NOT NULL,
                humidity REAL NOT NULL,
                cloud_cover INTEGER NOT NULL,
                wind_condition REAL NOT NULL,
                precipitation BOOLEAN NOT NULL,
                remarks TEXT
            )
        ''')
        conn.commit()

def save_to_csv(data):
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        file_empty = file.tell() == 0
        if file_empty:
            writer.writeheader()
        writer.writerow(data)

def insert_data_into_db(weather_data):
    with sqlite3.connect('weather_data.db') as conn:
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO weather (city, timestamp, temperature, humidity, cloud_cover, wind_condition, precipitation, remarks)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (weather_data['city'], weather_data['timestamp'], weather_data['temperature'],
                  weather_data['humidity'], weather_data['cloud_cover'], weather_data['wind_condition'],
                  int(weather_data['precipitation']), weather_data['remarks']))
            conn.commit()
            print("Data inserted:", weather_data)
        except Exception as e:
            print(f"Error inserting data into DB: {e}")

def main():
    setup_database()
    
    cities = ['Hong Kong', 'New York', 'Tokyo', 'London', 'Sydney']
    print(f"Fetching weather data for: {', '.join(cities)}")

    interval = int(input("Enter the interval in minutes (default is 1): ") or 1)
    duration = int(input("Enter how long to fetch data (in minutes, default is 10): ") or 10)

    end_time = time.time() + (duration * 60)

    for city in cities:
        schedule.every(interval).minutes.do(fetch_weather_data, city)

    print(f"Scheduler started. Fetching weather data every {interval} minute(s) for {duration} minute(s).")

    while True:
        schedule.run_pending()
        if time.time() > end_time:
            print("Time limit reached. Stopping the fetch process.")
            break
        time.sleep(1)

if __name__ == "__main__":
    main()