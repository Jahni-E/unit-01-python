#1 Simple Counter:
#I created a variable which is J converted it to 1 then I put it into a while loop makeing the variable < 11 to count up from 1 to 10
J = 1
while J < 11:
    print(J)
    J += 1

#2 Countdown:
#I created a variable which is M converted it to 10 then I put it into a while loop makeing the variable > 0 to count down from 10 to 1
M = 10
while M > 0:
    print(M)
    M -= 1

#3 Factorial Calculation
# I made two variables which is number and result i made number a integer because im inputing a number.Then i made the result 1 i then put both of the variables into the while loop and multiplied the number variable and the result variable and subtract the number by 1 because i wanted  a output of factors
number = int(input("give me a number"))
result = 1
while number> 0:
    result = number * result
    number -= 1

print(result)


#4 Password Game:
# I made two variables which is Guess and password then i put both of these variables in my while loop and in my while loop i put if the Guess is != password print you got it right but if not print guess the password again
Guess = input("guess the password")
password = "Programming_26"

while Guess != password:
    print("thats not correct")
    Guess = input("guess the password again")
else: 
    print("you got it right")


