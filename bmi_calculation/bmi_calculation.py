
# Program: BMI Calculator
# File Name: bmi_calculation.py

# Description:
#   This program calculates a user's Body Mass Index (BMI) based on
#   their weight (kg) and height (m). It also determines the user's
#   BMI category (Underweight, Normal weight, Overweight, Obese)
#   and whether their BMI is considered healthy.

# Input:
#   - Name (string)
#   - Weight in kilograms (float)
#   - Height in meters (float)
#
# Output:
#   - Formatted BMI report containing:
#       * User's name
#       * Rounded weight (kg)
#       * Rounded height (m)
#       * Calculated BMI value
#       * BMI Category
#       * Health Status (True / False)




def calculate_bmi():
    # Get user's name
    user_name = input("Name: ")

    # Get weight in kg
    weight_kg = float(input("Weight (kg): "))
    rounded_weight = round(weight_kg, 1)

    # Get height in meters
    height_m = float(input("Height (m): "))
    rounded_height = round(height_m, 2)

    # Calculate BMI
    bmi_value = weight_kg / (height_m ** 2)
    rounded_bmi = round(bmi_value, 1)

    #Determine category correctly
    if bmi_value < 18.5:
        bmi_category = "Underweight"
    elif 18.5 <= bmi_value < 25:
        bmi_category = "Normal weight"
    elif 25 <= bmi_value < 30:
        bmi_category = "Overweight"
    else:
        bmi_category = "Obese"

    # Determine health status
    is_healthy = (bmi_category == "Normal weight")

    # Print result (formatted output as required)
    print(f"\n--- BMI Report for {user_name} ---")
    print(f"Weight: {rounded_weight:.1f} kg")
    print(f"Height: {rounded_height:.2f} m")
    print(f"BMI: {rounded_bmi:.1f}")
    print(f"Category: {bmi_category}")
    print(f"Healthy? {is_healthy}")

    return rounded_bmi, rounded_weight, rounded_height, user_name, bmi_category, is_healthy


# Run function and display returned values
calculate_bmi()

