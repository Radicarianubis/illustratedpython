# Basic calculator for two numbers w/exception handling
def get_valid_number(prompt):
    while True:
        value = input(prompt)
        try:
            value = float(value)
        except ValueError:
            print(f"Sorry, you entered {value} which is not a valid number. Try again: ")
            continue
        else:
            break
    return value

def get_valid_operator(prompt):
    while True:
        value = input(prompt)
        if value not in {'+', '-', '*', '/'}:
            print(f"Sorry, you entered {value} which is not a valid operator. Try again: ")
            continue
        else:
            break
    return value

def execute_operation(num1, num2, operator):
    while True:
        if operator == '+':
            value = num1 + num2
        elif operator == '-':
            value = num1 - num2
        elif operator == '*':
            value = num1 * num2
        elif operator == '/':
            try:
                value = num1 / num2
            except ZeroDivisionError:
                num2 = get_valid_number("Your second operand was 0, you cannot divide by zero. Please choose a different number: ")
                continue
        break
    return value

x = get_valid_number("Please enter the first number: ")
y = get_valid_number("Please enter the second number: ")
z = get_valid_operator("Please enter the operation you want to perform: ")
final = execute_operation(x, y, z)
print(final)

