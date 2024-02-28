"""Write a program that opens a file, reads its contents, and writes the contents to a new file.
 Use a try-except-finally block to ensure that the file is closed even if an exception occurs during the file operations."""


def copy_file_contents(source_filename, target_filename):
    try:
        with open(source_filename, 'r') as source_file:
            content = source_file.read()

        with open(target_filename, 'w') as target_file:
            target_file.write(content)
            print(f"Successfully copied from '{source_filename}' to '{target_filename}'.")

    except FileNotFoundError:
        print(f"Error: File '{source_filename}' not found.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        source_file.close()
        target_file.close()

try:
    source_file_name = input("Enter the source file name: ")
    target_file_name = input("Enter the target file name: ")
    copy_file_contents(source_file_name, target_file_name)

except Exception as e:
    print(f"An error occurred: {e}")

