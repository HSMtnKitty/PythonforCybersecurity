"""
This script will ask for name, quest, and favorite color
"""

def collect_user_data():
    print("You must answer me these questions three!!")
    name = input("What is your name?: ")
    quest = input("What is your quest?: ")
    color = input("What is your favorite color?")

    #return collected info as a dictionary
    return {
        "Name":name,
        "Quest": quest,
        "Color": color

    }

#Function to save information to a file
def save_to_file(data, filename="grail.txt"):
    with open(filename, "w") as file:
        for key, value in data.items():
            file.write(f"{key}: {value}:\n")
    print(f"You May Pass! Information has been saved to {filename}")

#Collect and save user info
save_to_file(collect_user_data())