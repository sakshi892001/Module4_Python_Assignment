import math

try:
    number = float(input("Enter a number: "))
    if number < 0:
        print("Error: Square root and logarithm are not defined for negative numbers.")
    else:
        square_root = math.sqrt(number)
        natural_log = math.log(number)
        sine = math.sin(number)
        print(f"Square root of {number}: {square_root:.4f}")
        print(f"Natural logarithm of {number}: {natural_log:.4f}")
        print(f"Sine of {number} (in radians): {sine:.4f}")
except ValueError:
    print("Error: Please enter a valid number.")
