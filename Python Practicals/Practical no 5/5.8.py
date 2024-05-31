'''5.8Write a python program to demonstrate a implementation static method.'''
class Calculator:
  @staticmethod
  def add_numbers(num1, num2):
    return num1 + num2

# call the static method without creating an object
sum = Calculator.add_numbers(5, 7)
print('Sum:', sum)
