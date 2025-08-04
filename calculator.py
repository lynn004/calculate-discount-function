# This is a simple calculator program
# It asks the user for two numbers and an operation, then shows the result

# Asking the user to enter the first number
num1 = input("Enter the first number: ")
num1 = float(num1)  # converting the input to a number

# Asking the user to enter the second number
num2 = input("Enter the second number: ")
num2 = float(num2)  # converting the input to a number

# Asking the user to choose the operation
print("Choose the operation you want to perform:")
print("+ for addition")
print("- for subtraction")
print("* for multiplication")
print("/ for division")
operation = input("Enter the operation: ")

# Doing the calculation depending on the choice of operation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    # making sure not to divide by zero
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Cannot divide by zero"
else:
    result = "Invalid operation"

# Showing the result
print(f"{num1} {operation} {num2} = {result}")
