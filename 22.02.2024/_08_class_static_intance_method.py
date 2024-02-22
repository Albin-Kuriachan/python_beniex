"""show class method, static method and instance method with simple example."""


"Instance method"
class Instance_method:
    def __init__(self,name):
        self.name = name

obj = Instance_method("Alan")
result = obj.name
print(result)


"Class method"
class Class_method:
    def __init__(self, name):
        self.name = name

    @classmethod
    def data(cls, name):
        return cls(name)

obj = Class_method.data("Amal")
result = obj.name
print(result)

"Static method"
class Student1:
    @staticmethod
    def data(name):
        return Instance_method(name)

obj = Student1.data("Alan")
result = obj.name
print(result)
