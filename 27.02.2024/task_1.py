
"""Create a class called Add , it must have __call__ defined. Create an object of that class.
When the object is directly called with a list of integers - like - obj([1,2,3,4,5]) It must return the sum
of elements in the list.
Eg:
add = Add()
total = add([1,2,3,4,5,6])"""


class Add:
    def __call__(self,input_list):
        return sum(input_list)


obj = Add()
input_list =[1,2,3,4,5,6]
total=obj(input_list)
print(total)
