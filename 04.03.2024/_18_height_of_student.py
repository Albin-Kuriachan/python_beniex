""".Python program to for student height record for a school using Class and Objects."""


class Student:
    height_record = {}

    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.record_height()

    def record_height(self):
        Student.height_record[self.name] = self.height


def main():
    while True:
        name = input("Enter the student's name (or 'quit' to exit): ")

        if name == "quit":
            break

        height = input("Enter the student's height in centimeters: ")
        try:
            height = int(height)

        except ValueError:
            print("Invalid height. Please enter a numeric value.")
            continue

        student = Student(name, height)
        print("Height recorded for", name)
    print()
    print("Student height records:")
    for name, height in Student.height_record.items():
        print(f"{name}: {height} cm")


if __name__ == "__main__":
    main()
