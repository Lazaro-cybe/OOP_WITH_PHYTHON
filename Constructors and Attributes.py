# car_class.py

class Car:
    # Constructor
    def __init__(self, make, model, year):
        # Instance attributes
        self.make = make
        self.model = model
        self.year = year

    # Method to display car details
    def display_info(self):
        print(f"This car is a {self.year} {self.make} {self.model}.")

# Create Car objects
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Tesla", "Model S", 2022)

# Call method to show info
car1.display_info()
car2.display_info()

