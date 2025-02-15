# 1. Step
number1 = int(input("Please enter the first number:"))

# 2. Step
print("Operations")
print("1 Addition")
print("2 Subtraction")
print("3 Multiplication")
print("4 Division")
operation = int(input("Please choose a number between 1 and 4:"))

# 3. Step
number2 = int(input("Please enter the second number:"))

# 4. Step
def calculate(value1, value2, operation):
    if (operation == 1):
        return value1 + value2
    elif (operation == 2):
        return value1 - value2
    elif (operation == 3):
        return value1 * value2
    elif (operation == 4):
        return value1 / value2

if (1 <= operation <= 4):
    result = calculate(number1, number2, operation)
    print(number1, "with", number2, "operation no:", operation, "result:", result)
else:
    print("The number you entered must be between 1 and 4")
