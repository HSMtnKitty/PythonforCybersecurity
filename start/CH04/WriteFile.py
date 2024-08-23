#!/usr/bin/env python3
# Sample script that writes to a file
# By Heather

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

#open file fkor writing
f = open(dir_path + "/hackme.txt", "w")

#write to the file
print("hello world\n")
f.write("")


#close file
f.close()