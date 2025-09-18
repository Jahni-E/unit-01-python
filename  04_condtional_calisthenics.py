#Exercise1
x = 14
if x > 10:
    print(True)
else:
    print(False)
#Exercise2
x = 15
y = "student"
if x < 18 or y:
    print(10)
else:
    print(20)
#Exercise3
fruit = ["banna", "apple", "mango"]
if "banna" in fruit:
    print("yes")
else:
    print("no")
#Exercise5
weight = input("weight:")
zone = input("zone:")
if weight < 0:
    print("Error: invalid weight")
    if zone == "a":
        print(f"your shipping cost is : ${weight * 5}")
        if zone == "b":
            print(f"your shipping cost is : ${weight * 7}")
            
#Exercise6
