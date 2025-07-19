import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]+ "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My To-Do App")
st.subheader("Manage your tasks efficiently")
st.write("Welcome to your to-do list!")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo.strip(), key=index)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        st.rerun()

st.text_input(label = "",placeholder="Enter a new task", on_change=add_todo, key="new_todo")



