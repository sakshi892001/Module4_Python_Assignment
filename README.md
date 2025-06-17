## Module 4: Functions and Modules in Python

## Overview

This repository contains two Python scripts for the Module 4 assignment of the Tutedude Python course, focusing on functions and modules:

1. **factorial.py**: Defines a function to calculate the factorial of a given number using a loop and prints the result for a sample input.

2. **math_calculations.py**: Uses the math module to calculate the square root, natural logarithm, and sine of a user-provided number.

## Prerequisites

- Python 3.x installed (verify with `python --version`).
- Git installed (verify with `git --version`).
- Visual Studio Code (VS Code) with Git extension enabled.

## Repository Setup

1. **Clone the Repository**:

- Clone this repository to your local machine:

     ```bash
     git clone https://github.com/sakshi892001/Module4_Python_Assignment.git

2. **Navigate to the Repository Folder:**

     ```bash
     cd Module4_Python_Assignment

3. **Run the scripts**:

      ```bash
     python factorial.py
     python math_calculations.py

## Task 1: Calculate Factorial Using a Function

- File: factorial.py
- Functionality: Defines a function factorial that calculates the factorial of a number using a loop. Calls the function with a sample number (5) and prints the result. Handles invalid inputs (e.g., negative numbers).

## Task 2: Using the Math Module for Calculations

- File: math_calculations.py
- Functionality: Takes a number as user input and uses the math module to calculate its square root, natural logarithm, and sine (in radians). Displays the results with error handling for invalid inputs (e.g., negative numbers for logarithm or square root).

## Error Handling

- Task 1:
  - Checks for negative numbers in the factorial function.
  - Catches unexpected errors during function execution

- Task 2:
  - Validates input for negative numbers (invalid for square root and logarithm).
  - Catches ValueError for non-numeric inputs.
  - Handles general exceptions with user-friendly messages.

## Notes

- Ensure Python is installed and added to your system's PATH.

- Test the scripts with various inputs to verify robustness.
