import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import numpy as np
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


def analyze_weather_data(city_choice):
    try:
        df = pd.read_csv('weather_data.csv')
        city_data = df[df['city'].str.lower() == city_choice.lower()]
        
        if city_data.empty:
            messagebox.showerror("Error", f"No data available for {city_choice}.")
            return
        
        stats = city_data.describe()
        result = stats.to_string()
        messagebox.showinfo(f"Analysis for {city_choice}", result)

    except (pd.errors.ParserError, FileNotFoundError) as e:
        messagebox.showerror("Error", str(e))

def visualize_weather_data(cities):
    with sqlite3.connect('weather_data.db') as conn:
        query = """
            SELECT city, 
                   AVG(temperature) AS avg_temp, 
                   AVG(humidity) AS avg_humidity, 
                   AVG(cloud_cover) AS avg_cloud_cover, 
                   AVG(wind_condition) AS avg_wind_condition
            FROM weather 
            WHERE city IN ({})
            GROUP BY city
        """.format(','.join('?' for _ in cities))
        
        df = pd.read_sql_query(query, conn, params=cities)

    if df.empty:
        messagebox.showerror("Error", "No data available for the selected cities.")
        return

    plot_bar_chart(df, 'city', 'avg_temp', 'Average Temperature in Selected Cities (°C)', 'Temperature (°C)', 'skyblue')
    plot_bar_chart(df, 'city', 'avg_humidity', 'Average Humidity in Selected Cities (%)', 'Humidity (%)', 'lightgreen')
    plot_bar_chart(df, 'city', 'avg_wind_condition', 'Average Wind Condition in Selected Cities (m/s)', 'Wind Speed (m/s)', 'salmon')


def compare_weather_conditions(cities):
    with sqlite3.connect('weather_data.db') as conn:
        query = """
            SELECT city, 
                   AVG(temperature) AS avg_temp, 
                   AVG(humidity) AS avg_humidity, 
                   AVG(wind_condition) AS avg_wind_condition
            FROM weather 
            WHERE city IN ({})
            GROUP BY city
        """.format(','.join('?' for _ in cities))
        
        df = pd.read_sql_query(query, conn, params=cities)

    if df.empty:
        messagebox.showerror("Error", "No data available for the selected cities.")
        return

    df.set_index('city')[['avg_temp', 'avg_humidity', 'avg_wind_condition']].plot(kind='bar', figsize=(10, 6))
    plt.title('Comparison of Weather Conditions in Selected Cities')
    plt.ylabel('Average Values')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.legend(['Avg Temperature (°C)', 'Avg Humidity (%)', 'Avg Wind Speed (m/s)'])
    plt.show()

def plot_bar_chart(df, x_col, y_col, title, ylabel, color):
    plt.figure(figsize=(10, 6))
    plt.bar(df[x_col], df[y_col], color=color)
    plt.title(title)
    plt.xlabel('City')
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

def on_analyze_button_click(city_combobox):
    city_choice = city_combobox.get()
    analyze_weather_data(city_choice)

def on_visualize_button_click():
    cities = ['Hong Kong', 'New York', 'Tokyo', 'London', 'Sydney']
    visualize_weather_data(cities)

def on_compare_button_click():
    cities = ['Hong Kong', 'New York', 'Tokyo', 'London', 'Sydney']
    compare_weather_conditions(cities)

def create_gui():
    root = tk.Tk()
    root.title("Weather Data Analysis")

    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

    # City selection
    ttk.Label(frame, text="Select City:").grid(row=0, column=0, sticky=tk.W)
    city_combobox = ttk.Combobox(frame, values=['Hong Kong', 'New York', 'Tokyo', 'London', 'Sydney'])
    city_combobox.grid(row=0, column=1, sticky=(tk.W, tk.E))

    # Analyze button
    analyze_button = ttk.Button(frame, text="Analyze Weather Data", command=lambda: on_analyze_button_click(city_combobox))
    analyze_button.grid(row=1, column=0, columnspan=2)

    # Visualize button
    visualize_button = ttk.Button(frame, text="Visualize Weather Data", command=on_visualize_button_click)
    visualize_button.grid(row=2, column=0, columnspan=2)

    # Compare button
    compare_button = ttk.Button(frame, text="Compare Weather Conditions", command=on_compare_button_click)
    compare_button.grid(row=3, column=0, columnspan=2)

    # Exit button
    exit_button = ttk.Button(frame, text="Exit", command=root.quit)
    exit_button.grid(row=4, column=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    create_gui()


