from employee import employee_details

def test_employee_details():
    result = employee_details("Asha", "E101", "IT", 50000)
    expected = "Employee Name: Asha, ID: E101, Department: IT, Salary: 50000"
    assert result == expected