t=[]
L= 1
while True:
    print("Your current todos are ")
    for x in t:

        print(f"{L}.{x}")
        L += 1
    Q =input("Would you like to add or remove a todo or clear all or edit")
    if Q == "add":
        n = input("What is your new todo")
        t.append(n)
    if Q == "remove":
        x =input("What do you want to remove")
        t.remove(x)
    if Q == "clear all":
        t=[]
