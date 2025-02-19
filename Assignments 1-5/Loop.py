response = input("Is today a good day? y/n")
if response == 'y':
    for _ in range(10):
        print("Yes it is")
elif response == 'n':
    print("it will get better")
else:
    print("Please reinput y or n")