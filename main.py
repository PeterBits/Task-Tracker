import cmd
import os
from methods import (
    add_task,
    print_json,
    create_task_file,
    get_tasks,
    get_task_file,
    delete_task,
    update_task,
    get_params_for_update
)


class MyCLI(cmd.Cmd):
    prompt = '>> '  
    intro = 'Welcome to Task Tracker CLI of PeterBits. Type "help" for available commands.'  
    #  Python automatically looks for a method in your class named do_<command> and executes it if it exists.

    # Functions in the cmd.Cmd class must accept two arguments: self and an additional argument for user input after the command name, as required by the cmd module in Python. 
    def do_hello(self, _):
        print("Hello, World!")
        
    def do_clear(self, arg):
        os.system('cls' if os.name == 'nt' else 'clear')

    def do_quit(self, _):
        return True
    
    # Method on active task tracker CLI
    def  preloop ( self ): 
        task_file = get_task_file()
        if (not task_file): create_task_file()
    
    def do_list(self, _):
        task_list = get_tasks()
        print_json(task_list) if len(task_list) > 0 else print('Dont have tasks yet.')

    def do_add(self, line):
        add_task(line)

    def do_del(self, task_id):
        delete_task(task_id)
        
    def do_update(self, line):
        update_task(line)
    


   # run before the command is executed
    # def  precmd ( self, line ): 
        # return line.lower()  
    
    # def  postcmd ( self, stop, line ): 
    # run after the command is executed
        # return stop   


if __name__ == '__main__':
    MyCLI().cmdloop()