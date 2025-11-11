# BMI Calculator (Python)

This program calculates a user's Body Mass Index (BMI) and classifies their health status based on standard BMI ranges. The program prompts the user for their name, weight in kilograms, and height in meters, calculates the BMI value, determines the BMI category, and reports whether the user is considered healthy.


## Formula Used

bmi_value = weight_kg / (height_m ** 2)


## BMI Categories

BMI Range               Category        

BMI < 18.5         =  Underweight    
18.5 ≤ BMI < 25    =  Normal weight 
25 ≤ BMI < 30      =  Overweight     
BMI ≥ 30           =  Obese


## Program Behavior

The program:

1. Asks the user for:
   - Name  
   - Weight (kg)  
   - Height (m)

2. Calculates BMI and rounds:
   - Weight to **1 decimal place**
   - Height to **2 decimal places**
   - BMI to **1 decimal place**

3. Determines whether the user is in a **healthy** category (`Normal weight`).

4. Prints a formatted BMI report.

# How to Run

```bash
python3 gambling_game.py
