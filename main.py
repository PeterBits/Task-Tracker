import cmd
import os
import json


def create_task_file():
    with open('tasks_data.json', 'w') as json_file:
        json.dump([], json_file)

def get_tasks():
    file_list = os.listdir('./')
    tasks_file = [file_list for file_list in file_list if file_list.endswith('.json')][0]

    if tasks_file:
        file_path = os.path.join('./', tasks_file)
        print(f"Processing file: {tasks_file}")
        with open(file_path, 'r') as json_file:
            return json.load(json_file)
    else:
        return False


def already_has_the_task(new_task, task_list ):
    return any(task == new_task for task in task_list)
    

def add_task(task: str):
    task_list = get_tasks()
    if(already_has_the_task(task, task_list)):
        print("Already has the task...")
        return
    task_list.append(task)
    with open('tasks_data.json', 'w') as json_file:
        json.dump(task_list, json_file)
    print(f"Task added: {task}")

class MyCLI(cmd.Cmd):
    prompt = '>> '  
    intro = 'Welcome to Task Tracker CLI of PeterBits. Type "help" for available commands.'  
    
    def  preloop ( self ): 
        # TODO Add create file or write file before get task
        task_list = get_tasks()
    
    def  precmd ( self, line ): 
    # run before the command is executed
        return line.lower()  
    
    def  postcmd ( self, stop, line ): 
    # run after the command is executed
        return stop   
    
    #  Python automatically looks for a method in your class named do_<command> and executes it if it exists.
    def do_hello(self, line):
        print("Hello, World!")
    
    def do_add(self, line):
        print(line)
        add_task(line)


    def do_quit(self, line):
        return True
    
    def do_get_tasks(self, line):
        task_list = get_tasks()
        prtin(task_list)


if __name__ == '__main__':
    MyCLI().cmdloop()