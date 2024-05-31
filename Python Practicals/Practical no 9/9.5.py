'''9.5Programme to open a file in read mode and print number of
occurrences of character ‘a’'''
'''
def count_char_occurrences(file_path, char):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            char_count = content.count(char)
            return char_count
    except FileNotFoundError:
        return "File not found"

file_path = "text_file.txt"  # Replace with the path to your text file
char_to_count = 'a'
char_count = count_char_occurrences(file_path, char_to_count)

if isinstance(char_count, int):
    print(f"Number of occurrences of '{char_to_count}' in the file {file_path}: {char_count}")
else:
    print(char_count)
x
'''
def count_char_a(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            count = content.count('a')
            print(f"Number of occurrences of 'a' in the file: {count}")
    except FileNotFoundError:
        print("File not found.")

def main():
    file_path = input("Enter the path to the file: ")
    count_char_a(file_path)

if __name__ == "__main__":
    main()
