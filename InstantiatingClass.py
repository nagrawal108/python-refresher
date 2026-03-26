# Student class with name, age and marks attributes
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def __str__(self):
        return f"Student(name={self.name}, age={self.age}, marks={self.marks})"

    # Method to calculate grade based on marks
    def calculate_grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 80:
            return 'B'
        elif self.marks >= 70:
            return 'C'
        elif self.marks >= 60:
            return 'D'
        else:
            return 'F'

# Instantiate a Student object
student1 = Student("Alice", 20, 85)
print(student1)  # Output: Student(name=Alice, age=20, marks=85)
grade = student1.calculate_grade()
print(f"Marks: {student1.marks} -> Grade: {grade}")
        
    