"""Extend the above solution again and add another instance method called 'as_dict'. The method should return
 a dictionary with the data of the student. It should contain 'name', 'score', 'grade', keys and their respective values. """

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.grade = self.grade(score)

    def grade(self, score):
        if score >= 90:
            return "A+"
        elif 80 <= score < 90:
            return "A"
        elif 70 <= score < 80:
            return "B+"
        elif 60 <= score < 70:
            return "B"
        elif 50 <= score < 60:
            return "C+"
        elif 40 <= score < 50:
            return "C"
        else:
            return "FAILED"

    def display(self):
        print("Name:", self.name)
        print("Score:", self.score)
        print("Grade:", self.grade)

    def dict(self):
        return {
            'name': self.name,
            'score': self.score,
            'grade': self.grade
        }

student1 = Student("Albin", 85)
student2 = Student("Akhila", 15)

student1.display()
print()
student2.display()
print()
print("Student 1 :", student1.dict())
print("Student 2 :", student2.dict())
