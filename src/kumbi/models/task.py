from dataclasses import dataclass
from enum import Enum
from datetime import datetime

class Command(Enum):
    ADD = "add"
    UPDATE = "update"
    DELETE = "delete"
    MARK = "mark"
    LIST = "list"

class Argument(Enum):
    ID = "id"
    DESCRIPTION = "description"
    STATUS = "status"
    LIST = "list"


class Status(Enum):
    TODO = "todo"
    INPROGRESS = "in-progress"
    DONE = "done"

@dataclass
class Task:
    id: int # cannot be updated
    description: str
    status: Status
    createdAt: datetime #cannot be updated
    updatedAt: datetime