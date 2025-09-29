#Exercise1:
# the goal was to count from 1 to 10 so i wrote this code below
for x in range(11):
    print(x)

#Exercise2:
# the goal was to count from 900 to 1000 by 10 so i wrote the code below 
for x in range(900,1010, 10):
    print(x)

#Exercise3:
# the goal was to count up from 1 to 100 by 9 so i used a for loop and wrote the code bellow to get from 1 to 100 counting by 9
for x in range(1,109, 9):
    print(x)

#Exercise:5
rows = 5

for i in range(rows):
    for j in range(i + 1):
       print('*', end=' ')
print()
#The output of the code is * * * * * * * * * * * * * * * 