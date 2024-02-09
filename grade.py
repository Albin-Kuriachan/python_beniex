def calculate_grade(score):
    if score < 0 or score > 100:
        print("Invalid score.")
    elif score >= 90:
        print("Grade: A+")
    elif score >= 80:
        print("Grade: A")
    elif score >= 70:
        print("Grade: B+")
    elif score >= 60:
        print("Grade: B")
    elif score >= 50:
        print("Grade: C+")
    else:
        print("Failed")

# Taking input from the user
score = float(input("Enter the student's score: "))

# Calculating and printing the grade
calculate_grade(score)
