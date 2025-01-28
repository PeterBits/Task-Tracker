import cmd
from methods import add_task, print_json, create_task_file, get_tasks, get_task_file
# """
# task_example = {
#     id: 1,
#     description: "Limpiar la casa",
#     status: "todo" | "in-progress" | "done",
#     createdAt: 12/12/2020,
#     updatedAt: 14/12/2020,
# }
# """



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
        task_file = get_task_file()
        if (not task_file): create_task_file()
    
    def do_ls(self, _):
        task_list = get_tasks()
        print_json(task_list) if len(task_list) > 0 else print('Dont have tasks yet.')

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