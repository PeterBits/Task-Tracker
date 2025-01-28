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

    def do_hello(self, _):
        """Greets the user."""
        print("Hello, World!")
        
    def do_clear(self, _):
        """Clears the terminal."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def do_quit(self, _):
        """Exits the Task Tracker CLI."""
        return True

    def preloop(self):
        task_file = get_task_file()
        if not task_file:
            create_task_file()

    def do_list(self, _):
        """Displays all tasks."""
        task_list = get_tasks()
        print_json(task_list) if len(task_list) > 0 else print('No tasks available.')

    def do_add(self, line):
        """Adds a new task. Syntax: add "task description"."""
        add_task(line)

    def do_del(self, task_id):
        """Deletes a task by its ID. Syntax: del <id>."""
        delete_task(task_id)

    def do_update(self, line):
        """Updates a task description by its ID. Syntax: update <id> "new description"."""
        update_task(line)

    def do_help(self, arg):
        """Shows help information for commands."""
        if arg:
            cmd.Cmd.do_help(self, arg)
        else:
            print(
                "\nAvailable commands:\n"
                "  hello   - Greets the user.\n"
                "  clear   - Clears the terminal.\n"
                "  quit    - Exits the Task Tracker CLI.\n"
                "  list    - Displays all tasks.\n"
                "  add     - Adds a new task. Syntax: add \"task description\".\n"
                "  del     - Deletes a task by its ID. Syntax: del <id>.\n"
                "  update  - Updates a task description by its ID. Syntax: update <id> \"new description\".\n"
                "  help    - Shows help information for commands.\n"
            )

    # run before the command is executed
    # def  precmd ( self, line ): 
        # return line.lower()  
    
    # def  postcmd ( self, stop, line ): 
    # run after the command is executed
        # return stop   


if __name__ == '__main__':
    MyCLI().cmdloop()
