#Exercise1:
name = "basketball"
for x in name:
    print(x)

#Exercise2:
j = [10,15,20,11]
result = 0
for x in j:
    result += x

print(result)

#Exercise3
S = "I like to watch movies with other people"
words = S.split(" ")
for x in words:
    print(x)
    len(x)


#Excercise4
my_dict = {
"black":3,
"blue":1,
"red":5,
"green":10
}
    
for key,value in my_dict.items():
    print(key,value)