# OIBSIP
This repository contains a collection of three simple yet functional command-line applications written in Python. Each script is a self-contained tool designed to perform a specific task, demonstrating fundamental Python concepts such as user input, data handling, and external API integration.

📁 Repository Contents
The repository includes the following command-line utilities:

BMI Calculator (BMI_Calculator.py)
A simple script that prompts the user for their weight (in kilograms) and height (in meters) to calculate their Body Mass Index (BMI). It then classifies the result into one of several health categories (Underweight, Normal weight, Overweight, or Obese).

Password Generator (password_generator.py)
This tool creates strong, random passwords based on user-defined criteria. Users can specify the desired password length and choose which character types to include: letters, numbers, and symbols.

Weather App (weather_app.py)
A command-line weather application that fetches real-time weather data for a user-specified location. It uses a weather API to display key information such as temperature, humidity, and current weather conditions.

🚀 How to Run the Scripts
Each script can be run independently from your terminal.

Clone the repository:
git clone <repository_url>
cd <repository_folder>

Run the script:
python BMI_Calculator.py
python password_generator.py
python weather_app.py

⚙️ Prerequisites
Python: You need Python 3.x installed on your machine.

API Key: The Weather App also requires a free API key from a service like OpenWeatherMap. You must replace the placeholder "YOUR_API_KEY" in the weather_app.py file with your actual key to use the application.
# 1. Clone the repo and install dependencies
git clone https://github.com/vaishnavirawate/weather-cli.git
cd weather-cli
pip install -r requirements.txt

# 2. Get your free API key from https://home.openweathermap.org/api_keys

# 3. Set the key as an environment variable
export WEATHER_API_KEY="your_actual_api_key_here" # Mac/Linux
# set WEATHER_API_KEY="your_key_here" # Windows CMD
# $env:WEATHER_API_KEY="your_key_here" # Windows PowerShell

# 4. Run the app!
python weather.py London
