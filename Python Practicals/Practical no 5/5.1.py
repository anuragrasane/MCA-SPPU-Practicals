'''5.1Create a class employee with data members: name, department
and salary.
Create suitable methods for reading and printing employee
information.'''
# define the employee class
class Employee:
  # initialize the attributes
  def __init__(self, name, department, salary):
    self.name = name
    self.department = department
    self.salary = salary

  # read the attributes from user input
  def read_data(self):
    self.name = input("Enter name: ")
    self.department = input("Enter department: ")
    self.salary = float(input("Enter salary: "))

  # print the attributes in a formatted way
  def print_data(self):
    print(f"Name: {self.name}")
    print(f"Department: {self.department}")
    print(f"Salary: {self.salary}")

# create an employee object
emp = Employee("John", "IT", 50000)

# print the employee data
emp.print_data()

# read new data for the employee
emp.read_data()

# print the updated employee data
emp.print_data()
