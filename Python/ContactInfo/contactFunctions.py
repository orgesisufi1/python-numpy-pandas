import mysql.connector 
import re
import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
database = os.getenv('DB_NAME')


con = mysql.connector.connect(
    host=host,
    user=user,
    passwd=password,
    database=database
)

cur = con.cursor()

def insertValues(values):
    name_regex = r"^[A-Za-z]+([-'\s][A-Za-z]+)*$"
    phone_regex = r"^\+?\(?\d{1,4}\)?[\s.-]?\d{1,4}[\s.-]?\d{1,4}[\s.-]?\d{1,4}$"
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    name = input("Please enter your name: ")
    if re.match(name_regex, name):
        values += (name,)
    else:
        print("Invalid input!")
        return values

    phone = input("Please enter your phone number: ")
    if re.match(phone_regex, phone):
        values += (phone,)
    else:
        print("Invalid input!")
        return values

    email = input("Please enter your email address: ")
    if re.match(email_regex, email):
        values += (email,)
    else:
        print("Invalid input!")
        return values

    opt_email = input("Please enter an optional email address: ")
    if re.match(email_regex, opt_email):
        values += (opt_email,)
    else:
        print("Invalid input!")
        return values

    return values


def addContact():
    try:
        add_values = ()
        add_values = insertValues(add_values) 
        insert_query = ("INSERT INTO Contacts (name, phone_number, email, optional_address) VALUES (%s, %s, %s, %s)")
        cur.execute(insert_query, add_values)
        con.commit()
        print("Information added successfully!")
    except ValueError as e:
        print("Insert a Valid Value", e)



def viewContacts():
    cur.execute("SELECT * FROM Contacts")

    for row in cur:
        print(row)

def updateContact():
    try:
        contact_id = int(input("Please provide the ID of the contact that you want to update: "))
        cur.execute("SELECT id FROM Contacts")
        all_id = [ ]
        for id in cur:
            all_id.append(id[0])

        if contact_id in all_id:
            update_values = ()
            update_values += insertValues(update_values)
            update_values += (contact_id,)
            update_query = """UPDATE Contacts 
                        SET name= %s, phone_number = %s , email = %s, optional_address = %s 
                        WHERE Contacts.id = %s"""
            
            cur.execute(update_query, update_values)
            con.commit()
            print(f"Contact with id: {contact_id}, updated successfully ")
        else:
            print(f"User with ID: {contact_id} does not exist!")
    except ValueError as e:
            print("Value Error! ", e)



def deleteContact():
    try:
        contact_id = int(input("Please provide the ID of the contact that you want to delete: "))
        cur.execute("SELECT id FROM Contacts")
        all_id = [ ]
        for id in cur:
            all_id.append(id[0])
        if contact_id in all_id:
            contact_id = (contact_id,)
            delete_query = """
            DELETE FROM Contacts
            WHERE id = %s
            """
            cur.execute(delete_query, contact_id)
            con.commit()
            print(f"User with ID: {contact_id[0]} is sucessfully deleted from the database!")
        else:
            print(f"User with ID: {contact_id[0]} does not exist!")
    except ValueError as e:
        print("Value Error! ", e)


updateContact()