def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

try:
    n=int(input("Enter a number: "))
    result = factorial(n)
    print(f"The factorial of {n} is: {result}")
except Exception as e:
    print(f"Error: {e}")