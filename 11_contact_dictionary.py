Contacts = {}

while True:
    print("1.Add Contact")
    print("2.Delete contact")
    print("3.List contacts")
    print("4.Exit")
    Choice=input("Enter your choice")
    if Choice == "1":
        name = input("Enter the Contacts name")
        phone = input("Enter the Contacts phone number")
        Contacts[name] = phone
        Contacts[phone]= name
        print("Contact added successfully!")
    if Choice == "2":
        D = input("Enter the name of the comntact to delete")
        print("Contact deleted successfully")
    if Choice == "3":
         for name in Contacts:
            print(Contacts[name])
         for phone in Contacts:
             print(Contacts[phone])
    if Choice == "4":
        print("Successfully exited")

