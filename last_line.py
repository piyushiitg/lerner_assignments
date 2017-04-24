"""
Assignment 1:
Last line

Ask the user for the name of a text file. Display the final line of that file.

The solution will be e-mailed to you tomorrow.  Meanwhile, think of ways in which you can solve this problem, and how it might relate to your daily work with Python.

"""

import sys
import os
def get_last_line_sol1(file_name):
    file_handle = open(file_name, "r")
    last_line = ""
    for line in file_handle.xreadlines():
        last_line = line
    return last_line

def get_last_line_sol2(file_name):
    file_handle = open(file_name, "r")
    return file_handle.readlines()[-1]

def get_last_line_sol3(file_name):
    # Using Fseek
    file_handle = open(file_name, "r")
    return file_handle.readlines()[-1]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Error: Please tell the file name, Run: python last_lone.py <file_name>"
        sys.exit(0)
    file_name = sys.argv[1]
    if not os.path.exists(file_name):
        print "Error: File does not exist on this location"
        sys.exit(0)
    print get_last_line_sol1(file_name)
    print get_last_line_sol2(file_name)

def lerner_solution():
    # Lerner Solution:
    filename = raw_input("Enter a filename: ")
    print(open(filename).readlines()[-1])
