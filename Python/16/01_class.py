# Class: Class is a blueprint or a template. Example: For for an Exam that contains name, age, elective, father's name etc

# Object: Object is an instance created from the template (class). Example: Form which contains the data for John Doe


class Employee:
    company = "Google"  # Class variable
    
    def get_salary(self): # self is important here because self is a way to reference the object of the class which is being created
        # print(self)
        return 34000  # Instance method
    
e1 = Employee()  # Creating an object of the class Employee
print(e1.company)  # Accessing class variable using object
print(e1.get_salary())  # Accessing instance method using object

e2 = Employee()
print(e2.company)
print(e2.get_salary())