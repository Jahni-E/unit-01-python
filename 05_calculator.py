#Welcome to the Calculatinator-inator 9000!
number1=float(input("Enter the first number"))
number2=float(input("Enter your second number"))

print("1.Addition")

print("2.Subtraction")

print("3.Multiplication")

print("4.Division")

print("5.Floor Division")

print("6.Exponential")

print("7.Remainder")

Choice=input("Enter your choice")

if Choice == "1":
    print(number1 + number2)

if Choice == "2":
    print(number1 - number2)

if Choice == "3":
    print(number1 * number2)

if Choice == "4":
    if number2 == 0:
        print("Error")
        
else:
    print(number1 / number2)

if Choice == "5":
    print(number1 // number2)

if Choice == "6":
        print(number1 ** number2)

if Choice == "7":
     print(number1 % number2)
 
