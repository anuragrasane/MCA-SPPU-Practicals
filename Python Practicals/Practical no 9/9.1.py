#9.1 Write a python program to get the file size of a plain text file
import os
def get_file_size(file_path):
    if os.path.isfile(file_path):
        file_size=os.path.getsize(file_path)
        return file_size
    else:
        return "file not found"
file_path="yourfile.txt"
file_size = get_file_size(file_path)
print(f"The size of the file {file_path} is: {file_size} bytes")
