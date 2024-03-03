"Search for a String in a Text File"


class Read_text:

    def __init__(self, filename, string):
        self.filename = filename
        self.string = string

    def contents(self):
        try:
            with open(self.filename, 'r') as file:
                for i in file:
                    word_split = i.split()
                    if self.string in word_split:
                        print(f'"{self.string}" is in the file "{self.filename}"')
                        break

                    return print(f'"{self.string}" is not in the file "{self.filename}"')


        except FileNotFoundError:
            print(f"The file '{self.filename}' not found")

        finally:
            print("Program finished")


path = input("Enter the path of the file to read:")
string = input("Enter the word to  search:")
obj = Read_text(path, string)
obj.contents()
