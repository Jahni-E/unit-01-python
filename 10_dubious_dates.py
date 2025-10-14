from datetime import datetime
#Exercise 1 
my_dt = datetime.now()
print(my_dt)

#Exercise 2
my_dt = datetime.now()
my_string = my_dt.strftime("%m/%d/%Y")
print(my_string)

#Exercise 3
my_string = "10/14/2025"
my_dt = datetime.strptime(my_string,"%m/%d/%Y")
print(my_dt)
New = "11/21/2025"
P = datetime.strptime(New,"%m/%d/%Y")
print(P)
d = my_dt - P
print(d)

#Exercise 4
B= input("What is your birthdate?")
my_dt = datetime.strptime(B,"%m/%d/%Y")
K = datetime.now()
M = K - my_dt
print(M)
