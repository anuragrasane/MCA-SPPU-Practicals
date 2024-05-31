'''10.3Write a python program to append data to an existing file
‘python.txt. Read data to be appended from the use, then display
the contents of entire file.'''
'''
# Function to append data to an existing file
def append_to_file(file_name, data):
    with open(file_name, 'a') as file:
        file.write(data + '\n')

# Read data to be appended from the user
data_to_append = input("Enter the data to append to the file: ")

# Append data to the file
append_to_file('python.txt', data_to_append)

# Display the contents of the entire file
print("Contents of the entire file 'python.txt':")
with open('python.txt', 'r') as file:
    content = file.read()
    print(content)
'''
def append_to_file(filename, data):
    try:
        with open(filename, 'a') as file:
            file.write(data)
            print("Data appended successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_file_contents(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(f"Contents of {filename}:\n{contents}")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")  

def main():
    filename = 'python.txt'
    data_to_append = input("Enter data to append to the file: ")
    append_to_file(filename, data_to_append)
    read_file_contents(filename)

if __name__ == "__main__":
    main()
