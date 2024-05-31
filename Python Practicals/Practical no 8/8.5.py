'''8.5Write multithread program where one thread prints square numbers and
another thread prints cube of numbers'''
import threading
import time

# Function to print square numbers
def print_squares():
    for i in range(5):
        time.sleep(1)
        print(f"Square of {i} is {i**2}")

# Function to print cube numbers
def print_cubes():
    for i in range(5):
        time.sleep(1)
        print(f"Cube of {i} is {i**3}")

# Creating threads
t1 = threading.Thread(target=print_squares)
t2 = threading.Thread(target=print_cubes)

# Starting threads
t1.start()
t2.start()

# Waiting for both threads to complete
t1.join()
t2.join()

print("Done!")
