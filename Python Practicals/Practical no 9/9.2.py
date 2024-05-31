'''9.2Write a python program to read config
file and display the contents of entire file'''
def read_config_file(file_path):
    try:
        with open(file_path, 'r') as file:
            config_contents = file.read()
            return config_contents
    except FileNotFoundError:
        return "File not found"

file_path = "db.sqlite3"  # Replace with the path to your configuration file
config_contents = read_config_file(file_path)

print(f"Contents of the configuration file {file_path}:")
print(config_contents)


