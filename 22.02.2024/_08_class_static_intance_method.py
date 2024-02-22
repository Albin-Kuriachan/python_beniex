"""show class method, static method and instance method with simple example."""

class Methods:
    data ="Class_method"

# Instance method
    def __init__(self,name):
        self.name = name

    def instance_method(self):
        return self.name

# Class method
    @classmethod
    def class_method(cls):
        return cls.data

# Static method
    @staticmethod
    def static_method():
        print("Print this is a Static method")


name=Methods("Instance Method")
print(name.instance_method())
print(Methods.class_method())
Methods.static_method()
