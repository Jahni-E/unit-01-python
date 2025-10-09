import os
import sys

# Task 1 (os module):I wanted to print my cuurent folder working directory using the os module so i used the os.getcwd function
current_directory = os.getcwd()
print("the current directory is:",current_directory)
# # Task 2 (os module):I used the os.listdir function to Create a new directory called "test_folder" in the current directory,Then print a list of all files and directories in the current directory
listdir = os.listdir()
print(listdir)
# """
# Task 3 (os module):I used the os.path.exists and os.mkdir functions to checked if a directory name existed in my working directory and if it didnt i created one 
if os.path.exists("data"):
    print("Directory already exists")
else:
    current_directory = os.mkdir("data")

# """
# Task 4 (os.path module):I used the os.path.exists function to check if a file existed and if it didnt i printed File not found
if os.path.exists("config.txt"):
    print("path")
else:
    print("File not found")
# """
# Task 5 (sys module):I used the sys.version function to see the python version i was currently useing
print("Python versiom:")
print(sys.version)



# Task 6 (sys module): I used the sys.platform function to see what my python interpreter was running on 
Name_of_platform = sys.platform
if sys.platform == 'win32':
    print("Running on Windows.")
   
elif sys.platform == 'linux':
    print("Running on Linux.")
    
elif sys.platform == 'darwin':
    print("Running on macOS.")