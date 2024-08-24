#!/usr/bin/env python3
# Sample script that writes to a file
# By Heather

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

#open file fkor writing
f = open(dir_path + "/hackme.txt", "w")

#ask some questions

name = input("What is your name?")
color = input("What is your favorite color?")
pet = input("What was your first pet's name?")
mum = input("What is your mother's maiden name?")
school = input("What is your first school's name?")

#write to the file
print("thank you!\n")
f.write(name)
f.write(color)
f.write(pet)
f.write(mum)
f.write(school)

#close file
f.close()