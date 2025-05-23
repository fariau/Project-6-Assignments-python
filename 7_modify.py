# 7. access modifiers: public , private and protected
# public == name 
# private == ssn 
# protected == salaray

class Employee:
    def __init__(self, name , salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn
        
    def get__ssn(self):
        return self.__ssn
    
    def set_salary(self, new_salary):
        if new_salary > 0:
            self._salary = new_salary
        else:
            print("salary must be positive in number")
            
    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")
        
class Manager(Employee):
    def __init__(self, name, salary, ssn, department):
        super().__init__(name, salary, ssn)
        self.department = department
        
    def show_manager_info(self):
        print(f"Manager: {self.name}")
        print(f"Department: {self.department}")
        print(f"Protected Salary: {self._salary}")
        print(f"Acessing SSN via getter command: {self.get__ssn()}") #private variable
        
Manager1 = Manager("Faria", "15000", "0312-0000000", "Information Technology")
Manager1.show_manager_info()
Manager1.set_salary(20000)
print("Update salary:", Manager1._salary)

# print(Manager1.__ssn)
print("Private SSN via managed: ", Manager1._Employee__ssn)