def employee_details(name, emp_id, department, salary):
    return (f"Employee Name: {name}, ID: {emp_id}, "
            f"Department: {department}, Salary: {salary}")

if __name__ == "__main__":
    n = input("Name: ")
    i = input("ID: ")
    d = input("Department: ")
    s = input("Salary: ")
    print(employee_details(n, i, d, s))