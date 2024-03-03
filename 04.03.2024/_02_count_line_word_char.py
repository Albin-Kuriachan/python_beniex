"Count the Number of Lines, Words, and Characters in a Text File"


class Read_text:

    def __init__(self, filename):
        self.filename = filename
        self.lines = 0
        self.words = 0
        self.characters = 0

    def contents(self):
        try:
            with open(self.filename, 'r') as file:
                for i in file:
                    self.lines += 1

                    word_split = i.split()
                    self.words += len(word_split)

                    word_join = " ".join(word_split)
                    self.characters += len(word_join)

            print(f'Number of lines in the file {self.lines}')
            print(f'Number of words in the file {self.words}')
            print(f'Number of characters in the file {self.characters}')
            print()
            file.close()


        except FileNotFoundError:
            print(f"The file '{self.filename}' not found")

        finally:
            print("Program finished")


path = input("Enter the path of the file to read:")
obj = Read_text(path)
obj.contents()
