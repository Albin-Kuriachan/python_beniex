"""Write a Python program that prompts the user to enter their age. Define a custom exception calledInvalidAgeError
that is raised when the entered age is less than 0 or greater than 150. Handle the InvalidAgeError exception and
display an appropriate error message. """



class InvalidAgeError(Exception):
    def __init__(self, age):
        self.age = age
        super().__init__(f"Invalid age: {age}. Age must be between 1 and 150.")

def user_age():
    try:
        age = int(input("Enter your age: "))
        if age < 1 or age > 150:
            raise InvalidAgeError(age)
        print(f"Your age is: {age}")
    except ValueError:
        print("Invalid input. Please enter a valid integer for age.")
    except InvalidAgeError as e:
        print(e)

user_age()
