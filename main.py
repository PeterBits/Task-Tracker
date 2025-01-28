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
        with open(file_path, 'r') as json_file:
            return json.load(json_file)
    else:
        return print('Dont have tasks yet.')


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
    #  Python automatically looks for a method in your class named do_<command> and executes it if it exists.

    # Functions in the cmd.Cmd class must accept two arguments: self and an additional argument for user input after the command name, as required by the cmd module in Python. 
    def do_hello(self, _):
        print("Hello, World!")

    def do_quit(self, _):
        return True
    
    # Method on active task tracker CLI
    def  preloop ( self ): 
        create_task_file()
    
    def do_ls(self, _):
        task_list = get_tasks()
        print(task_list) if len(task_list) > 0 else print('Dont have tasks yet.')

    def do_add(self, line):
        add_task(line)

    


   # run before the command is executed
    # def  precmd ( self, line ): 
        # return line.lower()  
    
    # def  postcmd ( self, stop, line ): 
    # run after the command is executed
        # return stop   


if __name__ == '__main__':
    MyCLI().cmdloop()