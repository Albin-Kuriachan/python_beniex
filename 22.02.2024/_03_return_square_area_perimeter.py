'Write a Python class, Square, and define two methods that return the square area and perimeter.'


class Area_Perimeter():
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

    def perimeter(self):
        return 4 * self.side_length

length=int(input("Enter the length of the square :"))
data = Area_Perimeter(length)
print("Area of square:", data.area())
print("Perimeter of square:", data.perimeter())
