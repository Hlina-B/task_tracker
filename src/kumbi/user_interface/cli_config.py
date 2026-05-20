from kumbi.models.task import Command, Argument
import argparse

def get_cli_input() -> argparse.Namespace:
    paraser = argparse.ArgumentParser(description="Kumbi CLI Application to Track Tasks.")
    sub_paraser = paraser.add_subparsers(dest="command", help="Available Sub Commands: add, update, delete, mark, list\n")
    add_paraser = sub_paraser.add_parser(Command.ADD.value, help="Add a new task with a title")
    add_paraser.add_argument(Argument.DESCRIPTION.value, type=str, help="The task title.")
    update_paraser = sub_paraser.add_parser(Command.UPDATE.value, help="Update a task with an id")
    update_paraser.add_argument(Argument.ID.value, type=int, help="The Id of the task you want to update")
    update_paraser.add_argument(Argument.DESCRIPTION.value, type=str, help="The new description of the task")
    delete_paraser = sub_paraser.add_parser(Command.DELETE.value, help="Delete a task with an id")
    delete_paraser.add_argument(Argument.ID.value, type=int, help="The ID of the task you want to delete")
    mark_paraser = sub_paraser.add_parser(Command.MARK.value, help="Mark a task as 'in-progress' or 'done'. Default is 'todo'")
    mark_paraser.add_argument(Argument.ID.value, type=int, help="The ID of the task you want to mark")
    mark_paraser.add_argument(Argument.STATUS.value, type=str, help="The status you want to mark the task with")
    list_paraser = sub_paraser.add_parser(Command.LIST.value, help="List all the tasks. You can also list by status ('in-progress', 'done', 'todo)")
    list_paraser.add_argument(Argument.STATUS.value, nargs="?", type=str, help="Filiter by the status")
    return paraser.parse_args()