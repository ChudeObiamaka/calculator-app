def calculator(num1, num2):
    operator = input( "Enter the operator (+, -, *, /): ")
    
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        else:
            return num1 / num2
    else:
        return "Error: Invalid operator."

# test the function
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("The result is: ", calculator(num1, num2))
