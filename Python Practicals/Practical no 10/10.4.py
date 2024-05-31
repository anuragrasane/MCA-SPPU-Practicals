'''10.4Write a python program to read a text file and print
number of lines, words and characters.'''
'''
# Function to count lines, words, and characters in a file
def count_stats(file_name):
    with open(file_name, 'r') as file:
        lines = 0
        words = 0
        characters = 0

        for line in file:
            lines += 1
            words_list = line.split()
            words += len(words_list)
            characters += sum(len(word) for word in words_list)

    return lines, words, characters

# Name of the file to be processed
file_name = 'sample.txt'  # Update with your file name

# Get the statistics
line_count, word_count, character_count = count_stats(file_name)

# Print the statistics
print("Number of lines:", line_count)
print("Number of words:", word_count)
print("Number of characters:", character_count)
'''
def count_lines_words_characters(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            num_characters = sum(len(line) for line in lines)
            print(f"Number of lines: {num_lines}")
            print(f"Number of words: {num_words}")
            print(f"Number of characters: {num_characters}")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def main():
    filename = input("Enter the filename to read: ")
    count_lines_words_characters(filename)

if __name__ == "__main__":
    main()
