"""Write a program to check the validity of a password. Primary conditions for password validation:
- minimum 8 charecters
- The alphabet must be between [a-z]
- At least one alphabet should be of Upper Case [A-Z]
- At least 1 number or digit between [0-9].
- At least 1 character from [ _ or @ or $ ].

Examples:
Input : R@m@_f0rtu9e$
Output : Valid Password

Input : Rama_fortune$
Output : Invalid Password
Explanation: Number is missing

"""


def check_password(password):
    if len(password) < 8:
        print("Output : Invalid Password")
        return "Explanation: Password minimum 8 characters"

    if not any(char.isupper() for char in password):
        print("Output : Invalid Password")

        return "Explanation: Upper Case character is missing "

    if not any(char.islower() for char in password):
        print("Output : Invalid Password")
        return "Explanation: Lower Case  character is missing "

    if not any(char.isdigit() for char in password):
        print("Output : Invalid Password")
        return  "Explanation: Number is missing"

    if not any(char in "_@$" for char in password):
        print("Output : Invalid Password")
        return "Explanation: _@$ any of the characters is not included "

    for i in password:
        if ("0" <= i <= '9') or ('a' <= i <= 'z') or ('A' <= i <= 'Z') or (i in ["_", "@", "$"]):
            continue
        else:
            print(f'Explanation: {i} Wrong special character is added to password')

    return "Output : Valid Password"


password = input("Enter your password :")
print(check_password(password))
