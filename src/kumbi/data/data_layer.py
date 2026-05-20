from kumbi.models.task import Task, Status
from pathlib import Path
import json
import os

def read_task() -> dict[int, Task]:
    current_dir = Path(__file__).parent
    file_path = current_dir/"task.json"
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, 'r', encoding='utf-8') as file:
            json_data: dict[str, dict] = json.load(file)
            return {v['id']: __dict_to_task(v) for v in json_data.values()}

    return {}


def write_task(data: dict[int, Task]):
    current_dir = Path(__file__).parent
    file_path = current_dir/"task.json"
    if os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump({v.id:__task_to_dict(v)  for v in data.values()}, file)

def __dict_to_task(task: dict) -> Task:
    return Task(task['id'], task['description'], Status(task['status']), task['createdAt'], task['updatedAt'])

def __task_to_dict(task: Task) -> dict:
    return {"id": task.id, "description": task.description, "status": task.status.value, "createdAt": task.createdAt, "updatedAt": task.updatedAt}

