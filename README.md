# OIBSIP
This repository contains a collection of three simple yet functional command-line applications written in Python. Each script is a self-contained tool designed to perform a specific task, demonstrating fundamental Python concepts such as user input, data handling, and external API integration.

## 📁 Repository Contents

### 1. BMI Calculator (`BMI_Calculator.py`)
A simple script that calculates your Body Mass Index (BMI) and provides a health category based on World Health Organization (WHO) standards.

**Features:**
- Prompts for weight (in kilograms) and height (in meters).
- Calculates BMI and classifies it into:
  - Underweight
  - Normal weight
  - Overweight
  - Obese

### 2. Password Generator (`password_generator.py`)
A secure and customizable tool for generating strong, random passwords.

**Features:**
- User-defined password length.
- Option to include/exclude character types:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Symbols
- Uses cryptographically secure random number generation.

### 3. Weather App (`weather_app.py`)
A command-line application that fetches and displays real-time weather data for any city worldwide.

**Features:**
- Fetches data from the OpenWeatherMap API.
- Displays key information:
  - Temperature (°C)
  - "Feels like" temperature
  - Humidity (%)
  - Weather conditions (e.g., "Clear sky", "Scattered clouds")

---

## 🚀 Getting Started

### Prerequisites
- **Python 3.x** must be installed on your system.
- The Weather App requires a **free API key** from [OpenWeatherMap](https://home.openweathermap.org/api_keys).

### Installation & Usage

1.  **Clone the repository**
    ```bash
    git clone https://github.com/vaishnavirawate/weather-cli.git
    cd weather-cli
    ```

2.  **Install the required Python dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the scripts**
    Each utility runs independently. Navigate to the project directory and use one of the following commands:

    ```bash
    # Run the BMI Calculator
    python BMI_Calculator.py

    # Run the Password Generator
    python password_generator.py

    # Run the Weather App (requires setup below)
    python weather_app.py London
    ```

### ⚙️ Weather App Setup (Required)

The Weather App requires an API key for authentication. For security, **do not hardcode the key** into the script. Instead, set it as an environment variable:

**On Linux/macOS (Terminal):**
```bash
export WEATHER_API_KEY="your_actual_api_key_here"
```

**On Windows (Command Prompt):**
```cmd
set WEATHER_API_KEY="your_key_here"
```

**On Windows (PowerShell):**
```powershell
$env:WEATHER_API_KEY="your_key_here"
```

> **Important:** This environment variable is only active in your current terminal session. You will need to set it again if you open a new terminal window.

After setting the variable, you can run the app:
```bash
python weather_app.py "London"
```

---

## 🔧 Technologies Used

- **Python 3**
- **argparse** module (for command-line arguments)
- **requests** library (for API calls in the Weather App)
- **secrets** module (for secure password generation)
- **OpenWeatherMap API** (for weather data)

This portfolio demonstrates skills in **user input handling, API integration, environment variable security, and building functional CLI tools.**
