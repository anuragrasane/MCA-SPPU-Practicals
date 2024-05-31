'''10.1 Program to create a simple file and write some content in it.'''
def create_and_write_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"File '{file_path}' created and content written successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = "new_file.txt"
content_to_write = "This is some content that will be written to the file."

create_and_write_file(file_path, content_to_write)
'''
Output
File 'new_file.txt' created and content written successfully.
'''
