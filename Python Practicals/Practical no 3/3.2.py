'''3.2 Write a function that takes a single character
and prints ‘Given character is Vowel’ if it is a vowel,
and ‘Given character is not a vowel’ otherwise.'''
ch=input("Enter the Character: ")
if ch in('a','e','i','o','u','A','E','I','O','U'):
    print("Given String is Vowel")
else:
    print("Given String is Not Vowel")

'''
def check_vowel_or_accept_character(character):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if character.lower() in vowels:
        print("The given character ",character,"is a Vowel.")
    else:
        new_character = input("Enter another single character: ")
        if len(new_character) == 1:
            if new_character.lower() in vowels:
                print(f"The new character '{new_character}' is a vowel.")
            else:
                print(f"The new character '{new_character}' is not a vowel.")
        else:
            print("Please enter only a single character.")

# Test the function with different characters
check_vowel_or_accept_character('a')  # Output: The given character 'a' is a vowel.
check_vowel_or_accept_character('b')  # Prompts the user to enter another single character.
'''
