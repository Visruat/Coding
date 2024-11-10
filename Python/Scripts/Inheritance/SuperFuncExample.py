# parent class
class Person1():
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def display(self):
    print(self.name, self.age)

class Person2():
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def display(self):
    print(self.age, self.name)

# child class
class Student(Person2, Person1):
  def __init__(self, name, age):
    self.sName = name
    self.sAge = age
    # inheriting the properties of parent class
    super().__init__("Rahul", age)

  def displayInfo(self):
    print(self.sName, self.sAge)

obj = Student("Mayank", 23)
obj.displayInfo()
obj.display()