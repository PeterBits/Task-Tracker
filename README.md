# Task Tracker CLI

A command-line tool to manage tasks efficiently. Add, update, delete, and track tasks in states like `todo`, `in-progress`, or `done`.

---

## Features

- **Add Tasks**: Create tasks with descriptions.
- **Update Tasks**: Modify task descriptions.
- **Delete Tasks**: Remove tasks by ID.
- **Change Status**: Mark tasks as `todo`, `in-progress`, or `done`.
- **Filter Tasks**: View tasks filtered by status (`done`, `in-progress`, `todo`).
- **List All Tasks**: View all tasks in JSON format.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/PeterBits/Task-Tracker.git
   cd Task-Tracker
   ```

3. Run the CLI:
   ```bash
   python main.py
   ```

---

## Commands

- `add "task description"`: Add a new task.
- `list`: Display all tasks.
- `update <id> "new description"`: Update a task's description.
- `del <id>`: Delete a task by ID.
- `progress <id>`: Mark a task as `in-progress`.
- `done <id>`: Mark a task as `done`.
- `todo <id>`: Mark a task as `todo`.
- `list_done`: List tasks marked as `done`.
- `list_in_progress`: List tasks marked as `in-progress`.
- `list_todo`: List tasks marked as `todo`.
- `clear`: Clear the terminal.
- `quit`: Exit the CLI.

---

## Example Usage

1. **Add a Task**:

   ```plaintext
   >> add "Clean the house"
   Task added: Clean the house
   ```

2. **List Tasks**:

   ```plaintext
   >> list
   [
       {
           "id": "1",
           "description": "CLEAN THE HOUSE",
           "status": "todo",
           "created_at": "10:30 28/01/2025",
           "updated_at": "10:30 28/01/2025"
       }
   ]
   ```

3. **Update a Task**:

   ```plaintext
   >> update 1 "Wash the dishes"
   Task 1 updated successfully.
   ```

4. **Mark as Done**:
   ```plaintext
   >> done 1
   Task 1 marked as done.
   ```

---

## Testing

Run tests with:

```bash
pytest --cov=. --cov-report=term-missing
```

---

## Dependencies

- Python 3.8+
- `pytest`
- `pytest-cov`

