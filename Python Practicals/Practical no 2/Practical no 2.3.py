#2.3. Write a Python program to find the greater number between two numbers using a nested if-else statement.
num1=int(input('Enter First Number: '))
num2=int(input('Enter Second Number: '))
if num1 != num2:
    if num1 > num2:
     print(f"{num1} is greater than {num2}.")
    else:
     print(num2," is greater than",num1)
else:
    print("Both numbers are equal.")
