'''9.4Write a python program to read binary file and display the
contents of entire file'''
'''
def read_binary_file(file_path):
    try:
        with open(file_path,'rb') as file:
            file_contents=file.read()
            return file_contents
    except FileNotFoundError:
        return "file not found"
file_path="binary_file.bin"
file_contents=read_binary_file(file_path)
if isinstance(file_contents,bytes):
    print(f"Contents of the binary file{file_path}:")
    print(file_contents)
else:
    print(file_contents)
'''

def read_binary_file(file_path):
    try:
        with open(file_path, 'rb') as file:  # 'rb' mode for reading binary
            contents = file.read()
            print("Contents of the binary file:")
            print(contents)
    except FileNotFoundError:
        print("File not found.")

def main():
    file_path = input("Enter the path to the binary file: ")
    read_binary_file(file_path)

if __name__ == "__main__":
    main()
