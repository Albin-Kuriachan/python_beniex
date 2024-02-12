
# Define a function that accepts roll number and returns whether the student is present or absent.

def check_attendance(roll_number, attendance_records):
    if roll_number in attendance_records:
        return "Present" if attendance_records[roll_number] == "P" else "Absent"
    else:
        return "Roll number not found"

attendance_records = {
    101: "P",
    102: "A",
}

roll_number = int(input("Enter roll number: "))
attendance_status = check_attendance(roll_number, attendance_records)
print(f"Roll Number {roll_number}: {attendance_status}")
