"""Merge Multiple Text Files into One"""


class Read_text:

    def __init__(self, filename,filename2):
        self.filename = filename
        self.filename2 = filename2

    def contents(self):
        try:
            with open(self.filename,'a') as file:

                for filename2 in self.filename2:

                    with open(filename2, 'r') as file2:
                        file.write("\n"+file2.read())

            with open(self.filename,"r")as read_file:
                print(read_file.read())

                file.close()
        except FileNotFoundError:
            print(f"The file '{self.filename}' not found")

        finally:
            print("Program finished")

path = input("Enter the path of the file to read:")
path2 = input("Enter the path of the file to read:")
obj=Read_text(path,path2)
obj.contents()