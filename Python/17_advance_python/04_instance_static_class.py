class Employee:
    company = "Apple"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary 

    # Instance method (default)
    def print_info(self):
        print(f"The name is {self.name} and the salary is {self.salary}")
    
    # static method
    @staticmethod
    def sum(a,b):
        return a+b
    
    # class method
    @classmethod
    def print_company(cls):
        print(cls.company)
    
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company
    
e1 = Employee("Jack", 34285)
e2 = Employee("Jill", 34285)
# print(Employee.company)
# print(Employee.name) # This will Throw an error

# e1.print_info()
# e2.print_info()

# print(e2.sum(3,23))

e1.print_company()
e1.change_company("Asus")
# e1.print_company()
print(Employee.company)