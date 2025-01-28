import os
import json
from datetime import datetime


def print_json(data):
    print(json.dumps(data, indent = 4))
    
def get_task_file():
    file_list = os.listdir('./')
    tasks_file = [file_list for file_list in file_list if file_list.endswith('.json')]
    return tasks_file[0] if tasks_file else False
        
    

def create_task_file():
    with open('tasks_data.json', 'w') as json_file:
        json.dump([], json_file)

def get_tasks():
    tasks_file = get_task_file()

    if bool(tasks_file):
        file_path = os.path.join('./', tasks_file)
        with open(file_path, 'r') as json_file:
            return json.load(json_file)
    else:
        return print('Dont have tasks yet.')


def already_has_the_task(new_task, task_list ):
    return any(task == new_task for task in task_list)
    

def generate_unique_id(task_list):
    existing_ids = {obj['id'] for obj in task_list}
    unique_id = 1  
    while str(unique_id) in existing_ids:
        unique_id += 1  
    return str(unique_id) 

def add_task(task_description: str):
    task_list = get_tasks()
    
    new_task = {
        "id": generate_unique_id(task_list),
        "description": task_description.upper(),
        "created_at": datetime.now().strftime("%H:%M %d/%m/%Y"),
        "status": "todo",
        "updated_at": datetime.now().strftime("%H:%M %d/%m/%Y")
        
    }
    
    task_list.append(new_task)
    
    with open('tasks_data.json', 'w') as json_file:
        json.dump(task_list, json_file, indent=4)
    print(f"Task added: {task_description}")