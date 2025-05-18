# calculator_class.py

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Error: Division by zero"

# Example usage
calc1 = Calculator(10, 5)

print("Addition:", calc1.add())
print("Subtraction:", calc1.subtract())
print("Multiplication:", calc1.multiply())
print("Division:", calc1.divide())

# Another example with division by zero
calc2 = Calculator(10, 0)
print("Division with 0:", calc2.divide())

