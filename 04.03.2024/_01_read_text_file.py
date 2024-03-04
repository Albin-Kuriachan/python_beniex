" Read and Print the Contents of a Text File"



class Read_text:

    def __init__(self, filename):
        self.filename = filename

    def contents(self):
        try:
            with open(self.filename,'r') as file:
                print(file.read())
                file.close()
        except FileNotFoundError:
            print(f"The file '{self.filename}' not found")

        finally:
            print("Program finished")

path = input("Enter the path of the file to read:")
obj=Read_text(path)
obj.contents()