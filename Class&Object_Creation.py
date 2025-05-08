# person_class.py

class Person:
    # Class attributes
    species = "Homo sapiens"
  
    # Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to display person's info
    def introduce(self):
        print(f"My name is {self.name}, I am {self.age} years old.")

# Creating objects
person1 = Person("Alice", 22)
person2 = Person("Bob", 30)

# Accessing attributes and calling methods
person1.introduce()
person2.introduce()

# Accessing class attribute
print(f"All persons are of species: {Person.species}")
