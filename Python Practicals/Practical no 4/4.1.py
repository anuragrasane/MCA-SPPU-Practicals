import random
my_list = [1, 2, 3, 4, 5]
my_tuple = ('a', 'b', 'c', 'd', 'e')
my_string = 'hello'
print(random.sample(my_list, 2)) 
print(random.sample(my_tuple, 3))
print(random.sample(my_string, 4))

'''
import random
my_list = [1, 2, 3, 4, 5]
my_tuple = ('a', 'b', 'c', 'd', 'e')
my_string = 'hello'
print(random.choice(my_list)) # prints a random number from 1 to 5
print(random.choice(my_tuple)) # prints a random letter from a to e
print(random.choice(my_string)) # prints a random character from hello
'''
