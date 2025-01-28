import pytest
import os
import json
from datetime import datetime
from methods import (
    get_id_and_description,
    get_description_text,
    generate_unique_id,
    add_task,
    update_task,
    delete_task,
    mark_in_progress,
    mark_done,
    mark_todo,
    filter_by_status,
    TASK_STATUS,
    create_task_file,
    get_tasks,
    update_status
)

@pytest.fixture(autouse=True)
def setup_task_file():
    if os.path.exists('tasks_data.json'):
        os.remove('tasks_data.json')
    create_task_file()

def test_get_id_and_description():
    task_id, description = get_id_and_description('1 "Clean the house"')
    assert task_id == '1'
    assert description == 'Clean the house'

def test_get_description_text():
    description = get_description_text('"Clean the house"')
    assert description == 'Clean the house'

def test_generate_unique_id():
    task_list = [{"id": "1"}, {"id": "2"}]
    unique_id = generate_unique_id(task_list)
    assert unique_id == '3'

def test_add_task():
    add_task('"Clean the house"')
    tasks = get_tasks()
    assert len(tasks) == 1
    assert tasks[0]["description"] == "CLEAN THE HOUSE"
    assert tasks[0]["status"] == "todo"

def test_update_task():
    add_task('"Clean the house"')
    update_task('1 "Wash the dishes"')
    tasks = get_tasks()
    assert len(tasks) == 1
    assert tasks[0]["description"] == "Wash the dishes".upper()

def test_delete_task():
    add_task('"Clean the house"')
    delete_task("1")
    tasks = get_tasks()
    assert len(tasks) == 0

def test_mark_in_progress():
    add_task('"Clean the house"')
    mark_in_progress("1")
    tasks = get_tasks()
    assert tasks[0]["status"] == TASK_STATUS["IN_PROGRESS"]

def test_mark_done():
    add_task('"Clean the house"')
    mark_done("1")
    tasks = get_tasks()
    assert tasks[0]["status"] == TASK_STATUS["DONE"]

def test_mark_todo():
    add_task('"Clean the house"')
    mark_todo("1") 
    mark_todo("1") 
    tasks = get_tasks()
    assert tasks[0]["status"] == TASK_STATUS["TODO"]

def test_filter_by_status():
    add_task('"Clean the house"')
    add_task('"Wash the car"')
    mark_done("1")
    todo_tasks = filter_by_status(TASK_STATUS["TODO"])
    done_tasks = filter_by_status(TASK_STATUS["DONE"])
    assert len(todo_tasks) == 1
    assert len(done_tasks) == 1
    assert done_tasks[0]["description"] == "CLEAN THE HOUSE"
    assert todo_tasks[0]["description"] == "WASH THE CAR"
