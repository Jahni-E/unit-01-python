# Task 1
def my_function(name):
    print("Hello" + name)

my_function("Jahni")


#Task 2
def add_num(number):
    return number ** 2

print(add_num(5))

#Task 3
def is_even (number):
    return number % 2 == 0
print(is_even(3))

#Task 4
def add_num(a,b):
    return a * b
x = add_num(6,7)
print(x)

#Task 5
def celsius_to_fahrenheit(celsius):
 fahrenheit = (celsius * 9/5) + 32
 return fahrenheit

print(celsius_to_fahrenheit(7))

#Task 6
def list_of_numbers(numbers):
   if not numbers:
      return 0 
   total = sum(numbers)
   average = total/(numbers)
   return average

#Task 7
