'''9.3Write a python program to read first.txt file and display the
contents of entire file'''
def read_file(file_path):
    try:
        with open(file_path,'r') as File:
            file_contents=file.read()
            return file_contents
    except FileNotFoundError:
        return "file not found"
file_path = "first.txt"
file_contents=read_file(file_path)
print(f"Contents of the configuration file{file_path}:")
print(file_contents)
