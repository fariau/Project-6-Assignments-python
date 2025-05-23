# 14. aggregation

class Employee:
    def __init__(self, name):
        self.name = name

    def get_details(self):
        return f"Employee: {self.name}"

class Department:
    def __init__(self, name, employee):
        self.name = name
        self.employee = employee 

    def show_department(self):
        return f"Department: {self.name}, {self.employee.get_details()}"

emp1 = Employee("Alice")
dept1 = Department("HR", emp1)

print(dept1.show_department()) 
