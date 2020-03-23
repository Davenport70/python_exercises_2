# Function for Fibonacci number

def Fibonacci(number):
    if number < 0:
        print("Incorrect input")
        # First Fibonacci number is 0
    elif number == 1:
        return 0
    # Second Fibonacci number is 1
    elif number == 2:
        return 1
    else:
        return Fibonacci(number - 1) + Fibonacci(number - 2)

print(Fibonacci(10))
