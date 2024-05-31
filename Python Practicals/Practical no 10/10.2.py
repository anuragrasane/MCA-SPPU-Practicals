#10.2Write a program to read contents of “first.txt” file and
#    write same content in “second.txt” file.

def read_and_write_file(input_file, output_file):
    try:
        with open(input_file, 'r') as file1:
            content = file1.read()
        
        with open(output_file, 'w') as file2:
            file2.write(content)
        
        print(f"Contents of '{input_file}' have been copied to '{output_file}' successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

input_file = "new_file.txt"
output_file = "second.txt"

read_and_write_file(input_file, output_file)
'''
Output
Contents of 'new_file.txt' have been copied to 'second.txt' successfully.
'''
