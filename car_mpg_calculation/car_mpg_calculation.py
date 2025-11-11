
#Program: Car MPG Calculation
# Description:
#   This program asks the user how many gallons of fuel were used
#   and how many miles were driven. It validates the input ranges
#   and calculates the car's MPG (Miles Per Gallon).

# Input:
#   - gallons_used (integer between 10 and 25)
#   - miles_driven (integer between 200 and 400)

# Output:
#   - MPG result and formatted explanation message




def miles_per_gallon():

    while True:
        gallons_used = int(input("Enter gallons used: "))
        
        if gallons_used < 10 or gallons_used > 25:
            print("Please enter a number from 10 to 25")
            continue
        break
    
    # Get miles driven (200–400)
    while True:
        miles_driven = int(input("Enter miles driven: "))

        if miles_driven < 200 or miles_driven > 400:
            print("Please enter a number from 200 to 400")
            continue 
        break
    
    # Calculate MPG
    car_mpg = miles_driven // gallons_used
    return car_mpg, gallons_used, miles_driven
    
car_mpg, gallons_used, miles_driven = miles_per_gallon()


print(f"If {gallons_used} gallons of gas is used to fuel a car, it should be able to travel {miles_driven} miles")
print(f"Gallons entered: {gallons_used}")
print(f"Miles entered: {miles_driven}")
