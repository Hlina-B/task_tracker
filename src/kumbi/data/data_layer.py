from kumbi.models.task import Task, Status
from pathlib import Path
import json
import os

def read_task() -> dict[int, Task]:
    current_dir = Path(__file__).parent
    file_path = current_dir/"task.json"
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, 'r', encoding='utf-8') as file:
            raw_data = json.load(file, object_hook=__json_to_task)
            return {v.id: v for v in raw_data.values()}
    return {}


def write_task(data: dict[int, Task]):
    current_dir = Path(__file__).parent
    file_path = current_dir/"task.json"
    with open(file_path, 'w', encoding='utf-8') as file:
        serialized = {
            k: {
                "id": v.id,
                "description": v.description,
                "status": v.status.value,
                "createdAt": v.createdAt,
                "updatedAt": v.updatedAt
            }
            for k, v in data.items()
        }
        json.dump(serialized, file, indent=4, ensure_ascii=False)

def __json_to_task(dct: dict) -> Task:
    if 'id' in dct and 'status' in dct: 
        return Task(
            id=int(dct['id']),
            description=dct['description'],
            status=Status(dct['status']),
            createdAt=dct['createdAt'],
            updatedAt=dct['updatedAt']
        )
    return dct