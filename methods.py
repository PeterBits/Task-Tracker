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

TASK_STATUS = {
    "TODO": 'todo',
    "IN_PROGRESS": "in-progress",
    "DONE": "done"
}

def get_current_time():
    return datetime.now().strftime("%H:%M %d/%m/%Y")

def get_id_and_description(line):
    match = re.search(r'^\s*(\d+)\s+"(.*?)"', line)  
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

def generate_unique_id(task_list):
    existing_ids = {obj['id'] for obj in task_list}
    unique_id = 1  
    while str(unique_id) in existing_ids:
        unique_id += 1  
    return str(unique_id) 

def update_status(task_id, new_status):
    task_list = get_tasks()
    task_list_updated = []
    for task in task_list:
        if(task["id"] == task_id):
            task_list_updated.append({
                **task,
                "status": new_status,
                "updated_at": get_current_time()
            })
        else:
            task_list_updated.append(task)
        
    with open('tasks_data.json', 'w') as json_file:
        json.dump(task_list_updated, json_file, indent=4)
    print(f"Task {task_id} in progress.")
    
def filter_by_status(status):
    task_list = get_tasks()
    return list(filter(lambda task : task["status"] == status , task_list))

def add_task(line):
    task_description = get_description_text(line)
    if(not task_description): 
        print('Invalid command for add task. Try: add "first task".')
        return
        
    task_list = get_tasks()
    new_task = {
        "id": generate_unique_id(task_list),
        "description": task_description.upper(),
        "created_at": get_current_time(),
        "status": "todo",
        "updated_at": get_current_time()
        
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
    task_id, description_task = get_id_and_description(line)
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
                "updated_at": get_current_time()
            }
            task_found = True
                
        task_list_updated.append(task)

    if not task_found:
        print(f"No task found with ID: {task_id}")
        return

    with open('tasks_data.json', 'w') as json_file:
        json.dump(task_list_updated, json_file, indent=4)

    print(f"Task {task_id} updated successfully.")
    
def mark_in_progress(task_id):
    update_status(task_id, TASK_STATUS["IN_PROGRESS"])
    
def mark_done(task_id):
    update_status(task_id, TASK_STATUS["DONE"])
    
def mark_todo(task_id):
    update_status(task_id, TASK_STATUS["TODO"])

def list_done_tasks():
    task_done = filter_by_status(TASK_STATUS["DONE"])
    print_json(task_done)
    
def list_in_progress_tasks():
    task_in_progress = filter_by_status(TASK_STATUS["IN_PROGRESS"])
    print_json(task_in_progress)
    
def list_todo_tasks():
    task_todo = filter_by_status(TASK_STATUS["TODO"])
    print_json(task_todo)