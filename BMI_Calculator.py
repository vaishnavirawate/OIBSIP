def get_valid_input(prompt, input_type=float, min_value=0.1, max_value=300):
    """
    Get validated user input with error handling
    """
    while True:
        try:
            value = input_type(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a value between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_bmi(weight, height):
    """
    Calculate BMI using the formula: weight (kg) / (height (m))^2
    """
    return weight / (height ** 2)

def classify_bmi(bmi):
    """
    Classify BMI with a unique system that includes more granular categories
    """
    if bmi < 16:
        return "Severely Underweight", "🔴 High health risk - Please consult a doctor"
    elif 16 <= bmi < 18.5:
        return "Underweight", "🟡 Moderate health risk - Consider nutritional guidance"
    elif 18.5 <= bmi < 22.9:
        return "Normal (Lower range)", "🟢 Low health risk - Maintain your healthy habits"
    elif 22.9 <= bmi < 24.9:
        return "Normal (Upper range)", "🟢 Low health risk - Continue your current lifestyle"
    elif 24.9 <= bmi < 27.5:
        return "Overweight (Lower range)", "🟠 Moderate health risk - Consider lifestyle adjustments"
    elif 27.5 <= bmi < 30:
        return "Overweight (Higher range)", "🟠 Moderate health risk - Recommended to make changes"
    elif 30 <= bmi < 35:
        return "Obese Class I", "🔴 High health risk - Medical advice recommended"
    elif 35 <= bmi < 40:
        return "Obese Class II", "🔴 Very high health risk - Consult healthcare provider"
    else:
        return "Obese Class III", "🔴 Extremely high health risk - Urgent medical attention advised"

def display_bmi_info(bmi, category, advice):
    """
    Display BMI results with visual formatting
    """
    print("\n" + "="*50)
    print("BMI CALCULATION RESULTS")
    print("="*50)
    print(f"Your BMI: {bmi:.1f}")
    print(f"Category: {category}")
    print(f"Health Advice: {advice}")
    print("="*50)

# Main program execution starts here
print("Welcome to the Advanced BMI Calculator!")
print("This tool will help you calculate your Body Mass Index")
print("and provide personalized health guidance.\n")

# Get user input
weight = get_valid_input("Enter your weight in kilograms (kg): ", min_value=20, max_value=300)
height = get_valid_input("Enter your height in meters (m): ", min_value=0.5, max_value=2.5)

# Calculate BMI
bmi = calculate_bmi(weight, height)

# Classify BMI
category, advice = classify_bmi(bmi)

# Display results
display_bmi_info(bmi, category, advice)

# Additional information
print("\nNote: BMI is a screening tool, not a direct measure of body fat.")
print("For a comprehensive health assessment, consult a healthcare professional.")