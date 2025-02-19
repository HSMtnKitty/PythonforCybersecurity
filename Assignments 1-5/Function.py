"""
This script demonstrates a function
"""

def send_message():
    """
    Prints a positive message for "y" response x10
    """
    for _ in range(10):
        print("It sure is!")

response = input("Is today a good day? y/n")

if response == 'y':
    #call function to print
    send_message()

elif response == 'n':
    print("it will get better")
else:
    print("Please reinput y or n")