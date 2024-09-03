# Weather Data Analysis Tool

A Python application that fetches weather data from the OpenWeatherMap API, stores it in a SQLite database, and allows users to analyze and visualize the data through a GUI.


## Features

- Fetches weather data for specified cities.
- Stores weather data in a CSV file and SQLite database.
- Analyzes weather data and provides statistical summaries.
- Visualizes average weather conditions using bar charts.
- Compares weather conditions across multiple cities.


## Prerequisites

- Python 3.x
- `pip` (Python package installer)


## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/weather-data-analysis.git
   cd weather-data-analysis

2. Install the required packages:

   ```bash
   pip install requests pandas matplotlib python-dotenv schedule

3. Create a .env file in the project directory and add your OpenWeatherMap API key:

   ```plaintext
   API_KEY=your_openweathermap_api_key


## Usage

1. Run the application:
   
   ```bash
    python main.py

2. Follow the prompts to enter the interval and duration for fetching weather data.

3. Use the GUI to analyze and visualize the weather data.


## Functions

- fetch_weather_data(city): Fetches weather data for a specific city.
- setup_database(): Sets up the SQLite database and table.
- save_to_csv(data): Saves weather data to a CSV file.
- insert_data_into_db(weather_data): Inserts weather data into the SQLite database.
- analyze_weather_data(city_choice): Analyzes and provides statistics for selected city data.
- visualize_weather_data(cities): Visualizes average weather data for selected cities.
- compare_weather_conditions(cities): Compares weather conditions across cities.


## Dependencies

- requests: For making HTTP requests to the OpenWeatherMap API.
- pandas: For data manipulation and analysis.
- matplotlib: For data visualization.
- python-dotenv: For loading environment variables from a .env file.
- schedule: For scheduling periodic tasks.


## License

This project is licensed under the MIT License. See the LICENSE file for details.


## Acknowledgments

- OpenWeatherMap for providing the weather data API.
- Python for the programming language used in this project.


## Contributing

Feel free to submit issues or pull requests for improvements and bug fixes.


### Notes

- Replace `yourusername` in the GitHub clone URL with your actual GitHub username.
- Make sure to create a `LICENSE` file if you decide to include a license for your project.

Let me know if you need any changes or additional information!# weather_pipeline
