'''12.5Write a NumPy program to get the dates of yesterday, today and
tomorrow.'''
import numpy as np
import datetime

# Get today's date
today = datetime.date.today()

# Calculate yesterday and tomorrow
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)
