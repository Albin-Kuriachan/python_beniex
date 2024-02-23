"""Create a class named Cypher. The purpose of that class is to receive an input string of characters and convert it to
another cypher string. Use a constructor to receive the input. You can also read the input from user. But don’t use
input() inside the constructor.
The class must have a class method to do the string conversion. And an instance method to invoke the classmethod
from within it.
• Use the below conversion logic:
• Iterate over each character in the string, and if the character is a digit increment it by one (0->1, 1-
>2, ... 9 should be replaced with 0)
• if the character is an alphabet then shift the character by 2 positions (use chr() and ord() built-ins for
this) (a->c, b->d, ... y->a, z->b) If the character is in upper case convert it to lower and vice versa
• The returned string must be of same length as the input.
No need to implement the reversing algorithm but will be a plus if available.
1) create an object for the Cypher class with the string.
2) call the instance method, which should internally call the classmethod you prepared for the conversion, pass the
string data to classmethod and do the conversion.
No need to consider special characters for now.
Expected output for the string "ABcD1293Z" is "cdEf2304b"""


class Cypher:

    def __init__(self, input_string):
        self.input_string = input_string

    @classmethod
    def convert_string(cls, string):
        """Converts the given string to cypher text."""
        converted_string = ""
        for i in string:
            if i.isdigit():
                char = str((int(i) + 1) % 10)
            elif i.isalpha():
                base = ord('a') if i.islower() else ord('A')
                char_code = (ord(i) - base + 2) % 26 + base
                char = chr(char_code)
                char = char.swapcase()
            else:
                char = i
            converted_string += char
        return converted_string

    def create_cypher(self):
        return self.convert_string(self.input_string)


cypher_obj = Cypher("ABcD1293ZY")
cypher_text = cypher_obj.create_cypher()
print(f'Input: {cypher_obj.input_string}')
print("Cypher text:", cypher_text)
