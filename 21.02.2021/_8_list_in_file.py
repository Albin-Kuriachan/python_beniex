'Write a Python program to write a list to a file. '


def list_in_file(path, input_list):

    with open(path, 'w') as file:
        for item in input_list:
          g=  file.write(str(item)+'\n' )
    print(f"The list has been written to '{path}' successfully.")


path = input("Enter the path of the file to write the list to: ")
list1 = [x for x in input("Enter the list of numbers separated by comma ,: ").split(",")]
list_in_file(path, list1)
