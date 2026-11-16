# To-Do List with File Storage

## 📌 Project Overview

A command-line To-Do List application built with Python that allows users to manage their daily tasks.

Users can add tasks, view existing tasks, mark tasks as completed, and delete tasks. Task information is stored in a JSON file so that it remains available even after the program is closed.

## ✨ Features

- Add new tasks with descriptions.
- View all saved tasks.
- Display task status as Pending or Completed.
- Mark tasks as completed.
- Delete tasks from the list.
- Automatically save changes to a JSON file.
- Load previously saved tasks when the program starts.
- Validate task descriptions and task numbers.
- Handle invalid JSON data and file-related errors.
- Preserve task data between program executions.

## 🧠 Concepts Practiced

- Python functions
- Lists and dictionaries
- `json` module
- `pathlib` module
- File handling
- Reading and writing JSON data
- Data persistence
- List methods such as `append()` and `pop()`
- `enumerate()` with custom starting indexes
- Conditional statements and loops
- Input validation
- Exception handling
- Modular programming

## 🛠️ Technologies Used

- Python 3
- JSON
- Python standard library

## ▶️ How to Run

Open a terminal in the repository directory and execute:

```bash id="4e7uwf"
python intermediate_python_programs/07_todo_list.py
```

The program automatically creates `tasks.json` in the same folder when tasks are saved.

## 📝 Sample Output

```text id="f4pgw9"
========================================
             TO-DO LIST
========================================
1. View Tasks
2. Add Task
3. Complete Task
4. Delete Task
5. Exit

Choose an option (1-5): 2
Enter task description: Complete Python project
Task added successfully!

========================================
               YOUR TASKS
========================================
1. [Pending] Complete Python project
```

*Note: The sample demonstrates adding and viewing a task. Actual task information depends on user input.*

## 🎯 Purpose

To understand how to build a practical task management application using Python while learning JSON-based data storage, file handling, data persistence, and error management.