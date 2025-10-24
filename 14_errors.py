#Example 1
def divide_numbers(num1,num2):
    try:
        result = 10/ 0
        print("Result:", result)
    except:
        print("you cant divide by zero")

#Example 2
def read_file(filename):
   try:
        file = open(filename, 'r')
        contents = file.read()
        print("File contents:", contents)
   except:
       print("no file found")
       
#Example 3
def get_item(lst, index):
    try:
         my_list = [1, 2, 3]
         print(my_list, 5)

    except:
       print("Index in list is out of range")

#Example 4
def get_value(dictionary, key):
    try:
         my_dict = {"a": 1, "b": 2}
         print(my_dict, "c")
    except:
            print("Dictionary c is not found")


#Example 5
def process_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File contents:", contents)
    except FileNotFoundError:
        print("Error: File not found.")
    else:
          print("File is found ")
    
    finally:
          print("File contents:", contents) 