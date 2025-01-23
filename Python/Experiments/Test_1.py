# Develop a program that picks up current path of execution and creates a file= .\Concepts\<InputFromUser>\<InputFromUser>.py

import os

print(__file__)
cwd = os.path.abspath(__file__)
print(cwd)
################################################
'''
os.path.abspath(__file__) = Gets the absolute path of the file being executed
os.path.dirname
'''