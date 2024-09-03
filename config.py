import yaml
import os
from dotenv import load_dotenv


load_dotenv()
print("Current working directory:", os.getcwd())
print("Files in the current directory:", os.listdir('.'))

try:
    with open('config.yml', 'r') as file:
        config = yaml.safe_load(file)
    print("Configuration loaded successfully.")
except FileNotFoundError as e:
    print(f"Error: {e}")


# # Load YAML configuration
# with open('/Users/ip.hau/Desktop/Data bootcamp/JDE/finished_project/weather_pipeline/config.yml', 'r') as file:
#     config = yaml.safe_load(file)

# print(config)

# # Accessing configuration values
# API_KEY = os.environ.get('API_KEY')  # Ensure your .env file has the API key
# cities = config['fetch']['cities']
# interval = config['fetch']['interval']
# duration = config['fetch']['duration']

# print(f"Cities to fetch: {cities}")
# print(f"Fetch interval: {interval} minutes")
# print(f"Fetch duration: {duration} minutes")