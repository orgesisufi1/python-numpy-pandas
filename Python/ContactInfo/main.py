from contactFunctions import *

print("""
1) Add Contact
2) Update Contact
3) Delete Contact
4) View Contacts
""")
operation = input("What operation would you like to execute: ")

if operation == "1":
    addContact()
elif operation == "2":
    updateContact()
elif operation == "3":
    deleteContact()
elif operation == "4":
    viewContacts()
else:
    print("Invalid Input! Please Try Again")