# Python code to demonstrate how parent constructors
# are called.

# parent class
class Person(object): # Object is a base class with no attritbutes and Methods

    # __init__ is known as the constructor
    def __init__(self, name: str, idnumber: int) -> None:
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)
        
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
    
# child class
class Employee(Person): # notice that Parent Class is passed as an argument to the Child class
    def __init__(self, name: str, idnumber: int, salary: int, post: str):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)
        
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        print("Post: {}".format(self.post))


# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")
b = Person("Visruat", 1234567)
# calling a function of the class Person using
# its instance
a.display()
b.display()
a.details()
b.details()
