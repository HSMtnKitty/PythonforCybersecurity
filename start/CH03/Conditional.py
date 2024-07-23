#Creates a script that promts the user to input y/n
answer = input("Is today a good day? (y/n): ")

#check if answer is yes or no
if answer == 'y':
    for _ in range (10):
        print("Yea it is")