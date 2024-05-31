#5.5Write a python program to demonstrate a superO.
# Define a parent class named Animal
class Animal:
    # Define a constructor with a name parameter
    def __init__(self, name):
        # Assign the parameter to the instance attribute
        self.name = name
    
    # Define a method to make a sound
    def make_sound(self):
        print(f"{self.name} makes a sound")

# Define a child class named Dog that inherits from Animal
class Dog(Animal):
    # Define a constructor with a name and a breed parameter
    def __init__(self, name, breed):
        # Call the parent class constructor with the name parameter using super()
        super().__init__(name)
        # Assign the breed parameter to the instance attribute
        self.breed = breed
    
    # Define a method to make a sound specific to dogs
    def make_sound(self):
        # Call the parent class method using super()
        super().make_sound()
        # Print an additional message
        print(f"{self.name} barks")

# Create an instance of the Dog class with name "Rex" and breed "German Shepherd"
dog = Dog("Rex", "German Shepherd")
# Call the make_sound() method
dog.make_sound()
