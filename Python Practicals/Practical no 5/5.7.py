'''5.7Write a python program to demonstrate a function overloading.'''
def add(a, b=None, c=None):
  if b is None and c is None: # one parameter
    return a
  elif c is None: # two parameters
    return a + b
  else: # three parameters
    return a + b + c


