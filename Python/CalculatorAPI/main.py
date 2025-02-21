import requests
import os 
from dotenv import load_dotenv

load_dotenv()

url = os.getenv('url')


def helloWorld():
    api = f'{url}/hello'
    try:
        response = requests.get(api)
        if response.status_code == 200:
            print(response.json())
        else:
            print("Something wrong happened. Please check again!")
    except Exception as e:
        print("Error! ", e)

def greetName():

    name =input("Please enter your name: ")
    api = f'{url}/greet?name={name}'
    try:
        response = requests.get(api)
        if response.status_code == 200:
            print(response.json())
    except ValueError as e:
        print("Error! Enter a valid Value", e)

def isAdult():
    try:
        name =input("Please enter your name: ")
        age = int(input("Please enter your age: "))
        api = f'{url}/people?name={name}&age={age}'
        response = requests.get(api)
        if response.status_code == 200:
            print(response.json())
    except ValueError:
        print("Error! Enter a valid value!")



def calculation():
    api = f'{url}/calculation'

    try:
        first_no = float(input("Please input the first number: "))
        second_no = float(input("Please input the second number: "))
        operations = ['+','-','*','/']
        operation = input("Input the operation you want to execute +,-,*,/: ")
        if operation not in operations:
            print("Please choose a valid operator!")
        else:
            inputs = {
            "first_number": first_no,
            "second_number": second_no,
            "operation": operation
            }

            response = requests.post(api, json=inputs)

            if response.status_code == 200:
                print("Response:", response.json())
            else:
                print("Failed to call the endpoint. Status code:", response.status_code)
                print("Error message:", response.text)
    
    except ValueError as e:
        print('Input a valid number please!')



isAdult()