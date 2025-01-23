import cmd
import os
import json


def create_task_file():
    with open('tasks_data.json', 'w') as json_file:
        json.dump([], json_file)

def get_tasks():
    # TODO REFACTOR
    file_list = os.listdir('./')
    if 'tasks_data.json' not in file_list:
        print(1)
        create_task_file()
        return False
    task_file = [file_list for file_list in file_list if file_list.endswith('.json')][0]

    if task_file:
        print(2)
        file_path = os.path.join('./', task_file)
        print(f"Processing file: {task_file}")

        try:
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                print(f"Data: {data}")
                if data != None:
                    
                    if(not len(data)):
                        print("Dont have tasks yet")
                        return False

                    
                    print(f"Data found: {data}")
                    return data

                else:
                    print(f"Data not found, creating new file")
                    return create_task_file()
            
        except Exception as e:
            print(f"Failed to process {task_file}: {e}")
    else:
        print("No task files found")
        return create_task_file()



class MyCLI(cmd.Cmd):
    prompt = '>> '  
    intro = 'Welcome to Task Tracker CLI of PeterBits. Type "help" for available commands.'  
    
    def  preloop ( self ): 
        get_tasks()
    
    def  precmd ( self, line ): 
    # run before the command is executed
        return line.lower()  
    
    def  postcmd ( self, stop, line ): 
    # run after the command is executed
        return stop   
    
    #  Python automatically looks for a method in your class named do_<command> and executes it if it exists.
    def do_hello(self, line):
        """Print a greeting."""
        print("Hello, World!")


    def do_quit(self, line):
        """Exit the CLI."""
        return True
    
    def do_get_tasks(self, line):
        """Get all tasks."""
        get_tasks()


if __name__ == '__main__':
    MyCLI().cmdloop()