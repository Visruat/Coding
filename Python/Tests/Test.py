# Python program to demonstrate 
# calling the parent's class method 
# inside the overridden method using 
# super() 
class Parent(object): 
    
    def show(self) -> str: 
        print("Inside Parent") 
        
class Child(Parent): 

    def __init__(self, Enable=True) -> None:
        self.Enable = Enable
    
    def show(self) -> str: 
        
        if(self.Enable):
            print("Inside Child") 
        else:
            super().show() 
        
        
# Driver's code 
obj = Child(False) 
obj.show() 
