FILEPATH = "todos.txt"
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass  # Create the file if it doesn't exist

def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg , filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

