#Write a Python program to accept a number from the user to check if the entered number is even or odd using an if-else statement.
# Accept a number from the user
num = int(input("Enter a number: "))

# Check if the number is even or odd
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")
