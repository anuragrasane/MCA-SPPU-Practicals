# 3.8 Python code to illustrate generators in Python.
# Author code to iterate generator in python

def CountDown(num):
    print("Starting CountDown from", num)
    while num > 0:
        yield num
        num -= 1

# Create a generator object
generator = CountDown(5)

# Iterate over the generated object
for i in generator:
    print(i)

# Output:
# Starting CountDown from 5
# 5
# 4
# 3
# 2
# 1

# completed successfully
