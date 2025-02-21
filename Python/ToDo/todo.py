import json
import os 
directory =  os.path.dirname(__file__)
filename = os.path.join(directory, 'todo.json')

json_outfile = filename

def addTask(json_path):
    #loading all the tasks first
    try:
        with open(json_path, 'r') as file:
            data = json.load(file)
            tasks = data["tasks"]
    except FileNotFoundError:
        print("File not found please check again!")


    task_name = input("Please enter the task name: ")
    task_description = input("Please enter the task desription: ")
    task_date = input("Please enter the task due date (DD-MM-YYYY): ")
    task_id = len(tasks) + 1
    task = {
            "id": task_id, 
            "name": task_name,
            "description": task_description, 
            "due_date": task_date, 
            "completed": False
            }
    
    #adding the task
    tasks.append(task)

    #putting it on the json file
    try:
        with open(json_path, 'w') as file:
            json.dump(data, file, indent=4)
    except FileNotFoundError:
        print("File bot found, please check again!")

def viewTask(json_path):
    #load all tasks to view
    try:
        with open (json_path, 'r') as file:
            data = json.load(file)
            tasks = data["tasks"]
            for row in tasks:
                print(row["id"])
    except FileNotFoundError:
        print("File bot found, please check again!")

        

def deleteTask(json_path, id):
    #empty list
    updated = [ ]

    #exctracting records for iteration
    try:
        with open (json_path, 'r') as file:
            data = json.load(file)
            tasks = data["tasks"]
            for row in tasks:
                print(row['id'])
                if int(row["id"]) != int(id):
                    updated.append(row)
    except FileNotFoundError:
        print("File not found, please check again!")
    
    #leaving the tasks list empty so it can append to updated records
    data["tasks"] = updated

    #inserting the data task with the updated record
    try:
        with open (json_path, 'w') as file:
            json.dump(data, file, indent=4)
    except FileNotFoundError:
        print("File not found, please check again!")

def markTask(json_path, id):
    #empty list
    updated_task = [ ]

    #loading the tasks first and appending it to the empty list above
    try:
        with open (json_path, 'r') as file:
            data = json.load(file)
            tasks = data["tasks"]
            for row in tasks:
                if int(row["id"]) == id:
                    row["completed"] = True
                    updated_task.append(row)
                else:
                    updated_task.append(row)
    except FileNotFoundError:
        print("File not found, please check again!")
        
    #overwriting the data
    data["tasks"] = updated_task

    #sending the data to the json file
    try:
        with open (json_path, 'w') as file:
            json.dump(data, file, indent=4)
    except FileNotFoundError:
        print("File not found, please check again!")

try:
    operation = input("Do you want to add (a), view (v), mark (m), delete (d) a task: ")
    if operation == 'a':
        addTask(filename)
    if operation == 'v':
        viewTask(filename)
    if operation == 'd':
        id = int(input("Please enter the task id that you want to delete: "))
        deleteTask(filename, id)
    if operation == 'm':
        id = int(input("Please enter the task id that you want to mark as completed: "))
        markTask(filename, id)
except ValueError as e:
    print(e, "Invalid input, please type an integer!")



