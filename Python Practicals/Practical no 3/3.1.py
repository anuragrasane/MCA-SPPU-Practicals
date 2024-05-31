# Example to demonstrate the use of built-in functions
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_numbers = sorted(numbers)
print("Sorted numbers: ",sorted_numbers)

#using the max function
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
max_number = max(numbers)
print("Maximum number: ",max_number)
               
# using the min function
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
min_number = min(numbers)
print("Minimum number: ",min_number)

#use the abs function
num1=int(input("Enter a number: "))
absolute_value = abs(num1)
print("the absoluate value of",num1,"is: ",absolute_value)

#Using len Function
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
length_of_list = len(numbers)
print("the length of numbers is: ",length_of_list)

'''
# Example to demonstrate understanding functions
def add_numbers(a, b):
    return a + b

num1 = 5
num2 = 3
result = add_numbers(num1, num2)
print("The sum of num1 and num is: ", result)

# Example to demonstrate the use of built-in functions
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_numbers = sorted(numbers)
max_number = max(numbers)
min_number = min(numbers)
print("Sorted numbers: ",sorted_numbers)
print("Maximum number: ",max_number)
print("Minimum number: ",min_number)

# Example to demonstrate a user-defined function
def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)

number = 5
factorial_result = calculate_factorial(number)
print("The factorial of number is: ", factorial_result)
'''
