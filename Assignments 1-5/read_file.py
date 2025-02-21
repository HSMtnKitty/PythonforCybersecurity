"""
Create script to disply info received from write_file.py
"""

#Function to read and display file content
def read_and_display_file(filename="grail.txt"):
    try:
        with open(filename, "r") as file:
            print("Here is some information: ")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: the file {filename} does not exist")


# Call the function to read the file
read_and_display_file()