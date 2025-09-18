grade =int(input("what grade is the student in"))
students =int(input("how many students are in line"))
Minutes =int(input("how much minutes until lunch period ends"))
lunchlist =input("is the student on the lunch list,")
Money =input("does student have lunch money")
# If statement was used to determine the amount of students on the line  and what grade there in to see if they get priority
if students > 30:
    if grade == 6 or grade==7 or grade==8:
        print("you get priority")
else:print("you dont get priority")
# If statement was used to determine if students have money or dont and if students are on the lunchlist or not on the lunch list
if lunchlist == "yes" or Money == "yes":
    print("you can get free lunch") 
else:
    print("you are not on the free lunch list or you need money")
# if statement was used to see if students have or dont have enough time in their lunch period
if students > 25:
    if Minutes >= 15:
        print('There is enough time')
    else:
         print("you do not have time left")