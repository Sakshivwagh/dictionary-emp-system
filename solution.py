# Solution
def is_valid_name(name):
    return name.replace(" ", "").isalpha()

def is_valid_age(age):
    return age.isdigit() and int(age) > 0

def add_employee(employees, emp_id, name, age, department):
    if emp_id in employees:
        print("Employee ID already exists!")
        return
    if not is_valid_name(name):
        print("Invalid name! Name should contain only alphabets and spaces.")
        return
    if not is_valid_age(age):
        print("Invalid age! Age should be a positive integer.")
        return
    employees[emp_id] = {"name": name, "age": int(age), "department": department}
    print("Employee added successfully!")

def remove_employee(employees, emp_id):
    if emp_id in employees:
        del employees[emp_id]
        print("Employee removed successfully!")
    else:
        print("Employee ID not found!")

def update_employee(employees, emp_id, name=None, age=None, department=None):
    if emp_id not in employees:
        print("Employee ID not found!")
        return
    if name and not is_valid_name(name):
        print("Invalid name format!")
        return
    if age and not is_valid_age(age):
        print("Invalid age format!")
        return
    if name:
        employees[emp_id]["name"] = name
    if age:
        employees[emp_id]["age"] = int(age)
    if department:
        employees[emp_id]["department"] = department
    print("Employee updated successfully!")

def search_employee(employees, key):
    key = key.lower()
    for emp_id, details in employees.items():
        if key in emp_id.lower() or key in details["name"].lower():
            print(f"ID: {emp_id}, Name: {details['name']}, Age: {details['age']}, Department: {details['department']}")
            return
    print("Employee not found!")

def sort_employees(employees, criteria):
    if criteria == "name":
        sorted_list = sorted(employees.items(), key=lambda x: x[1]["name"])
    elif criteria == "age":
        sorted_list = sorted(employees.items(), key=lambda x: x[1]["age"])
    elif criteria == "department":
        sorted_list = sorted(employees.items(), key=lambda x: x[1]["department"])
    else:
        print("Invalid sorting criteria!")
        return
    for emp_id, details in sorted_list:
        print(f"ID: {emp_id}, Name: {details['name']}, Age: {details['age']}, Department: {details['department']}")

def main():
    employees = {}
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Update Employee")
        print("4. Search Employee")
        print("5. Sort Employees")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            department = input("Enter Department: ")
            add_employee(employees, emp_id, name, age, department)
        elif choice == "2":
            emp_id = input("Enter Employee ID to remove: ")
            remove_employee(employees, emp_id)
        elif choice == "3":
            emp_id = input("Enter Employee ID to update: ")
            name = input("Enter new name (leave blank to keep unchanged): ") or None
            age = input("Enter new age (leave blank to keep unchanged): ") or None
            department = input("Enter new department (leave blank to keep unchanged): ") or None
            update_employee(employees, emp_id, name, age, department)
        elif choice == "4":
            key = input("Enter Employee ID or Name to search: ")
            search_employee(employees, key)
        elif choice == "5":
            criteria = input("Sort by (name/age/department): ")
            sort_employees(employees, criteria)
        elif choice == "6":
            print("Exiting Employee Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

------------------------------------------------------------------------------------------------------------------------------------------
Output-

Employee Management System
1. Add Employee
2. Remove Employee
3. Update Employee
4. Search Employee
5. Sort Employees
6. Exit
Enter your choice: 1
Enter Employee ID: 1
Enter Name: John doe
Enter Age: 34
Enter Department: CS
Employee added successfully!

Employee Management System
1. Add Employee
2. Remove Employee
3. Update Employee
4. Search Employee
5. Sort Employees
6. Exit
Enter your choice: 3
Enter Employee ID to update: 1
Enter new name (leave blank to keep unchanged): Sakshi Wagh
Enter new age (leave blank to keep unchanged): 23
Enter new department (leave blank to keep unchanged): IT
Employee updated successfully!

Employee Management System
1. Add Employee
2. Remove Employee
3. Update Employee
4. Search Employee
5. Sort Employees
6. Exit
Enter your choice: 4
Enter Employee ID or Name to search: Sakshi Wagh
ID: 1, Name: Sakshi Wagh, Age: 23, Department: IT

Employee Management System
1. Add Employee
2. Remove Employee
3. Update Employee
4. Search Employee
5. Sort Employees
6. Exit
Enter your choice: 1
Enter Employee ID: 2
Enter Name: Priti Jagtap
Enter Age: 23
Enter Department: CS
Employee added successfully!

Employee Management System
1. Add Employee
2. Remove Employee
3. Update Employee
4. Search Employee
5. Sort Employees
6. Exit
Enter your choice: 2
Enter Employee ID to remove: 2
Employee removed successfully!

Employee Management System
1. Add Employee
2. Remove Employee
3. Update Employee
4. Search Employee
5. Sort Employees
6. Exit
Enter your choice: 1
Enter Employee ID: 2
Enter Name: Radha Ghadage
Enter Age: 24
Enter Department: CS
Employee added successfully!

Employee Management System
1. Add Employee
2. Remove Employee
3. Update Employee
4. Search Employee
5. Sort Employees
6. Exit
Enter your choice: 5
Sort by (name/age/department): name
ID: 2, Name: Radha Ghadage, Age: 24, Department: CS
ID: 1, Name: Sakshi Wagh, Age: 23, Department: IT

Employee Management System
1. Add Employee
2. Remove Employee
3. Update Employee
4. Search Employee
5. Sort Employees
6. Exit
Enter your choice: 6
Exiting Employee Management System. Goodbye!
