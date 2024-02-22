
"Write a program to create a class by name Students, and initialize attributes like name, age, and grade while creating an object"

class Student:

    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

    def details(self):
        print(f"Student 1:Name:{self.name} Age:{self.age} Grade:{self.grade}")


obj = Student("Alan",25,"A")
obj.details()

