def sum_numbers(num1, num2):
    return num1 + num2

def average_numbers(*args):
    return sum(args) / len(args)

def power(base, exponent):
    return base ** exponent

def divide_numbers(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Cannot divide by zero!"

def multiply_numbers(*args):
    result = 1
    for num in args:
        result *= num
    return result
