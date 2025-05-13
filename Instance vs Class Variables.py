# student_class.py

class Student:
    # Class variable (shared across all instances)
    school_name = "Global Tech Academy"

    # Constructor with instance variables
    def __init__(self, name, student_id):
        self.name = name          # Instance variable
        self.student_id = student_id  # Instance variable

    # Method to display student info
    def display_info(self):
        print(f"Name: {self.name}, ID: {self.student_id}, School: {Student.school_name}")

# Creating student objects
student1 = Student("Asha", "BME001")
student2 = Student("John", "BME002")

# Display info for each student
student1.display_info()
student2.display_info()

# Change class variable for all students
Student.school_name = "International STEM Institute"

# Display again to see the updated class variable
student1.display_info()
student2.display_info()

