import streamlit as st
import functions


TODOS = functions.get_todos()

st.title("My To-Do App")
st.subheader("Manage your tasks efficiently")
st.write("Welcome to your to-do list!")



for index, todo in enumerate(TODOS):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        TODOS.pop(index)
        functions.write_todos(TODOS)
        st.experimental_rerun()

st.text_input(label = "",placeholder="Enter a new task", key="new_todo")


