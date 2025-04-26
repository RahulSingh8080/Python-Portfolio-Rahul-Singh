import streamlit as st
import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file if it exists."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            try:
                tasks = json.load(file)
            except json.JSONDecodeError:
                tasks = []
    else:
        tasks = []
    return tasks

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task_desc):
    tasks = load_tasks()
    task_dict = {
        "task": task_desc,
        "completed": False
    }
    tasks.append(task_dict)
    save_tasks(tasks)

def complete_task(task_index):
    tasks = load_tasks()
    tasks[task_index]['completed'] = True
    save_tasks(tasks)

def delete_task(task_index):
    tasks = load_tasks()
    tasks.pop(task_index)
    save_tasks(tasks)

# Streamlit App
st.title("📝 To-Do List App")

# Load tasks
tasks = load_tasks()

# Input to add a new task
with st.form("Add Task"):
    new_task = st.text_input("Enter a new task")
    submitted = st.form_submit_button("Add Task")
    if submitted and new_task.strip() != "":
        add_task(new_task)
        st.success(f"✅ Task '{new_task}' added successfully!")
        st.experimental_rerun()

# Display tasks
st.header("📋 Your Tasks")
if not tasks:
    st.info("No tasks available.")
else:
    for idx, task in enumerate(tasks):
        cols = st.columns([0.7, 0.15, 0.15])
        with cols[0]:
            st.text(task["task"])
        with cols[1]:
            if not task["completed"]:
                if st.button("✅ Complete", key=f"complete_{idx}"):
                    complete_task(idx)
                    st.experimental_rerun()
            else:
                st.markdown("✅ Completed")
        with cols[2]:
            if st.button("🗑️ Delete", key=f"delete_{idx}"):
                delete_task(idx)
                st.experimental_rerun()
