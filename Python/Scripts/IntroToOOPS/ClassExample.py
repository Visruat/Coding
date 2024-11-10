class Dog:

    # class attribute
    attr1: str= "mammal"

    # Instance attribute
    def __init__(self, name: str) -> None:
        self.name = name
        
    def __str__(self) -> str: 
        return(f"{self.attr1 = } and {self.name = }")

# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class methods
print(Rodger)
print(Tommy)