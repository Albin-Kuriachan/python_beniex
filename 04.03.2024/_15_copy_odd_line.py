"""Copy odd lines of one file to another file in Python"""


def copy_odd_lines(filename, copyfile):
    try:
        with open(filename, 'r') as file:
            with open(copyfile, 'w') as copyfile:
                lines = file.readlines()
                odd_lines = [i for x, i in enumerate(lines) if x % 2 == 0]
                copyfile.writelines(odd_lines)

    except FileNotFoundError:
        print(f"The file '{filename}' not found")


path = input("Enter the path of the file to read:")
copyfile = path + "_copy"
copy_odd_lines(path, copyfile)
