'''10.5Write a python program that reads a text file and changes the
file by capitalizing each character of file.'''
'''
# Function to capitalize each character in a file
def capitalize_file(file_name):
    modified_text = ""

    # Read the file and capitalize each character
    with open(file_name, 'r') as file:
        text = file.read()
        modified_text = text.upper()

    # Write the modified text back to the file
    with open(file_name, 'w') as file:
        file.write(modified_text)

# Name of the file to be processed
file_name = 'sample.txt'  # Update with your file name

# Capitalize each character in the file
capitalize_file(file_name)

print("File '{}' has been capitalized successfully.".format(file_name))
'''
def capitalize_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        capitalized_content = content.upper()
        with open(filename, 'w') as file:
            file.write(capitalized_content)
        print(f"File '{filename}' has been capitalized successfully.")
    except Exception as e:
        print(f"An error occurred while processing the file: {e}")

def main():
    filename = input("Enter the filename to capitalize: ")
    capitalize_file(filename)

if __name__ == "__main__":
    main()
