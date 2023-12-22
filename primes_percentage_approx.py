import math
from decimal import Decimal, getcontext

# Set the precision for Decimal calculations
getcontext().prec = 50  # Adjust the precision as needed

def calculate_expression():
    try:
        # Ask the user for a number
        user_input = float(input("Enter a number: "))
        
        if user_input <= 0:
            print("Invalid input. Please enter a positive number.")
            return

        # Calculate the expression number/log(number) using Decimal
        result = Decimal(user_input) / Decimal(math.log(user_input))
        
        # Calculate result2 using Decimal for more precision
        if math.log(user_input) > 0:
            result2 = Decimal(100) / Decimal(math.log(user_input))
        else:
            result2 = Decimal('nan')
        
        # Print the results with higher precision
        print(f"Result 1: {result}")
        print(f"Result 2: {result2}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Call the function to run the program
while True:
    calculate_expression()
