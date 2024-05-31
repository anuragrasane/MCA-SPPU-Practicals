#Program for performing CRUD operation with MongoDB and Python
import pymongo

# Connect to MongoDB (Make sure MongoDB is running)
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]  # Replace "mydatabase" with your desired database name
collection = db["employees"]  # Replace "employees" with your desired collection name

def create_employee():
    # Get input from user (e.g., ID, name, age, department, salary)
    employee_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    department = input("Enter employee department: ")
    salary = float(input("Enter employee salary: "))

    # Create a new document
    new_employee = {
        "employee_id": employee_id,
        "name": name,
        "age": age,
        "department": department,
        "salary": salary
    }

    collection.insert_one(new_employee)
    print("Employee added successfully!")

def read_employee():
    # Retrieve all employees from the collection
    for employee in collection.find():
        print(f"ID: {employee['employee_id']}, Name: {employee['name']}, Age: {employee['age']}, Department: {employee['department']}, Salary: {employee['salary']}")

def update_employee():
    # Get input from user (e.g., employee ID to update)
    employee_id_to_update = input("Enter employee ID to update: ")

    # Update the document (e.g., change name, age, department, or salary)
    new_name = input("Enter new employee name: ")
    new_age = int(input("Enter new employee age: "))
    new_department = input("Enter new employee department: ")
    new_salary = float(input("Enter new employee salary: "))

    collection.update_one({"employee_id": employee_id_to_update}, {"$set": {
        "name": new_name,
        "age": new_age,
        "department": new_department,
        "salary": new_salary
    }})

    print("Employee updated successfully!")

def delete_employee():
    # Get input from user (e.g., employee ID to delete)
    employee_id_to_delete = input("Enter employee ID to delete: ")

    # Delete the document
    collection.delete_one({"employee_id": employee_id_to_delete})
    print("Employee deleted successfully!")

# Menu loop
while True:
    print("\nMenu:")
    print("1. Add a new employee")
    print("2. View existing employees")
    print("3. Update employee details")
    print("4. Delete an employee")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        create_employee()
    elif choice == "2":
        read_employee()
    elif choice == "3":
        update_employee()
    elif choice == "4":
        delete_employee()
    elif choice == "5":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
'''
Output
Menu:
1. Add a new employee
2. View existing employees
3. Update employee details
4. Delete an employee
5. Exit
Enter your choice (1-5): 1
Enter employee ID: 2
Enter employee name: pratikmadane
Enter employee age: 23
Enter employee department: MCA
Enter employee salary: 50000
Employee added successfully!

Enter your choice (1-5): 2
ID: 2, Name: pratikmadane, Age: 23, Department: MCA, Salary: 50000.0

Enter your choice (1-5): 3
Enter employee ID to update: 2
Enter new employee name: Pratik Madane
Enter new employee age: 23
Enter new employee department: MCA
Enter new employee salary: 60000
Employee updated successfully!

Enter your choice (1-5): 2
ID: 2, Name: Pratik Madane, Age: 23, Department: MCA, Salary: 60000.0

Enter your choice (1-5): 4
Enter employee ID to delete: 2
Employee deleted successfully!

Enter your choice (1-5): 5
Exiting program. Goodbye!
'''
