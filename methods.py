import os
import json
import re
from datetime import datetime

# """
# task_example = {
#     id: 1,
#     description: "Limpiar la casa",
#     status: "todo" | "in-progress" | "done",
#     createdAt: 12/12/2020,
#     updatedAt: 14/12/2020,
# }
# """

def get_params_for_update(line):
    match = re.search(r'^\s*(\d+)\s+"(.*?)"', line)  
    print('Match encontrado:', match)  
    if match:
        return match.group(1), match.group(2)  
    return None, None  

def get_description_text(line):
    match = re.search(r'"(.*?)"', line)
    if match:
        return match.group(1)  
    return None  

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

def add_task(line):
    task_description = get_description_text(line)
    if(not task_description): 
        print('Invalid command for add task. Try: add "first task".')
        return
        
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
    
def delete_task(task_id):
    task_list = get_tasks()
    task_list_updated = list(filter(lambda task : task["id"] != task_id , task_list))
    with open('tasks_data.json', 'w') as json_file:
        json.dump(task_list_updated, json_file, indent=4)
    print(f"Task deleted: {task_id}" if len(task_list_updated) < len(task_list) else "Task dont found.")
    
def update_task(line):
    task_id, description_task = get_params_for_update(line)
    if not task_id or not description_task:
        print('Invalid input. Use the format: update <id> "<new description>".')
        return

    task_list = get_tasks()
    task_found = False
    task_list_updated = []
    for task in task_list:
        if task["id"] == task_id:
            task = {
                **task,
                "description": description_task,
                "updated_at": datetime.now().strftime("%H:%M %d/%m/%Y")
            }
            task_found = True
                
        task_list_updated.append(task)

    if not task_found:
        print(f"No task found with ID: {task_id}")
        return

    with open('tasks_data.json', 'w') as json_file:
        json.dump(task_list_updated, json_file, indent=4)

    print(f"Task {task_id} updated successfully.")
