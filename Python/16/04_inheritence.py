class Animal: # Parent class (superclass)
    location = "Australia"
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("Speaking now.....")

class Dog(Animal): # This is how inheritence is done in Python
    def speak(self):
        super().speak() # we are using speak method of parent class
        print("Woof!")

# a = Animal("Dog")
# a.speak()

d =  Dog("Bruno")
d.speak()
print(d.location)
