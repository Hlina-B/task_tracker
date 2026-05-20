# Kumbi Task Tracker

A decoupled Python Command Line Interface (CLI) application designed to track day-to-day tasks. Built following modern pythonic architectures, it relies on structured data contracts, separation of concerns, and native system pathing.

## Project Structure
kumbi_project/
├── pyproject.toml              # Modern package metadata & console entry points
├── .gitignore                  # Keeps clean environment/cache separation
└── src/
└── kumbi/
├── app.py              # Main execution engine entry point
├── user_interface/
│   └── cli_config.py   # Argparse CLI layout and subcommands
├── services/
│   └── task_services.py # Business logic dispatcher & task mutations
├── data/
│   └── data_layer.py   # File system persistence (JSON database)
├── models/
│   └── task.py         # Strongly typed Dataclasses and Enums
└── exceptions/
└── exception.py    # Custom application error constructs

## Installation
You can install this application natively in "Editable" mode to expose the `kumbi` command globally across your system machine environment:
```bash
pip install -e .

Usage Examples
1. Add a Task
kumbi add "workout"

2. List Tasks
List all recorded entries, or narrow your view by passing an optional status flag:
kumbi list
kumbi list in-progress

3. Update or Mark a Task Status
kumbi update 1 "practice python"
kumbi mark 1 done

4. Delete a Task
kumbi delete 1

Help:
example:
kumbi -h
kumbi add -h
kumbi list -h
