from datetime import datetime
from pprint import pprint
from kumbi.models.task import Command, Status, Task
from kumbi.data.data_layer import read_task, write_task
from kumbi.exceptions.exception import CommandError

tasks: dict[int, Task] = read_task()

def dispatcher(args):
    if args.command is None:
        raise CommandError("Command Cannot Be None. You must provide a command. Use 'kumbi -h' to see list of commands")

    match args.command:
        case Command.ADD.value:
            add_task(args.description)
        case Command.UPDATE.value:
            edit_task(args.id, args.description)
        case Command.DELETE.value:
            delete_task(args.id)
        case Command.MARK.value:
            mark_task(args.id, args.status)
        case Command.LIST.value:
            list_task(args.status)

def add_task(task_name: str):
    id = max(tasks.keys()) + 1 if len(tasks) > 0 else 1
    task = Task(id, task_name, Status.TODO, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), None)
    tasks.setdefault(id, task)
    write_task(tasks)
    print("Task added sucessfully. The status is todo")


def edit_task(id: int, description: str):
    value = tasks.get(id)
    if value is None:
        print("Update Unsuccessful. A task with the input ID doesn't exist")
        return
    value.description = description
    value.updatedAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    write_task(tasks)
    print("Update Sucessful.")


def delete_task(id: int):
    try:
        tasks.pop(id)
        write_task(tasks)
        print("Delete Sucessful.")
    except KeyError:
        print("Delete Unsuccessful. A task with the input ID doesn't exist")

def mark_task(id: int, mark: str):
    try:
        status = Status(mark)
        value = tasks.get(id)
        if value is None:
            print("Mark Unsuccessful. A task with the input ID doesn't exist")
            return
        
        if status.value == value.status.value:
            print(f"The task status is already {mark}. Doesn't need to be updated.")
            return
        
        value.status = status
        value.updatedAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        write_task(tasks)
        print("Status Marked Sucessfully.")
    except ValueError:
        print("Invalid status. Please check the status you can update to using -h")

def list_task(by: str = None):
    display = tasks
    filter_by = None
    is_by_all = by is None
    print(f"List Task By: {'All' if is_by_all else by} \n")
    
    if not is_by_all:
        filter_by = Status(by)
        display =  {v.id:v for v in tasks.values() if v.status.value == filter_by.value}
    pprint(display if len(display) else "No Task Found")

