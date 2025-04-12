class Employee:
    company = "Google" # This is class attribute
    def __init__(self, salary, name, bond, company):
        self.salary = salary # create an instance attribute of name salary and assign it with salary
        self.name = name
        self.bond = bond
        self.company = company

            
    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years")

e1 = Employee(34000, "John", 3, "Tesla")
print(e1.company) # will always print instance attribute whenever present
print(Employee.company) # This will always print class attribute because we use class name


#Object Introspection
print(dir(e1))