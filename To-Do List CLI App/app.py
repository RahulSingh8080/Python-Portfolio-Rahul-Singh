import streamlit as st
import json
import os

TASKS_FILE = "tasks.json"
tasks = []

def load_tasks():
    """Load tasks from JSON file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            try:
                global tasks
                tasks = json.load(file)
            except json.JSONDecodeError:
                tasks = []
    else:
        tasks = []

def save_tasks():
    """Save tasks to JSON file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task_desc):
    task_dict = {"task": task_desc, "completed": False}
    tasks.append(task_dict)
    save_tasks()

def complete_task(index):
    tasks[index]['completed'] = True
    save_tasks()

def delete_task(index):
    tasks.pop(index)
    save_tasks()

# ---------------- Streamlit app ----------------

st.title("📝 To-Do List App")

load_tasks()

# Add a new task
new_task = st.text_input("Enter a new task:")

if st.button("Add Task"):
    if new_task:
        add_task(new_task)
        st.success(f"Task '{new_task}' added!")
        st.rerun()  # <<=== updated here

# View tasks
st.subheader("Your Tasks:")

if tasks:
    for idx, task in enumerate(tasks):
        col1, col2, col3 = st.columns([6, 2, 2])
        with col1:
            st.write(f"{idx+1}. {task['task']} ({'✅' if task['completed'] else '❌'})")
        with col2:
            if not task['completed']:
                if st.button(f"✔️ Complete {idx+1}", key=f"complete{idx}"):
                    complete_task(idx)
                    st.success(f"Task {idx+1} marked completed!")
                    st.rerun()  # <<=== updated here
        with col3:
            if st.button(f"🗑️ Delete {idx+1}", key=f"delete{idx}"):
                delete_task(idx)
                st.warning(f"Task {idx+1} deleted!")
                st.rerun()  # <<=== updated here
else:
    st.info("No tasks available.")
