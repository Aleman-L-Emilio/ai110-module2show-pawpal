# app.py
import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

# Initialize Session State (Application Memory)
if "owner" not in st.session_state:
    st.session_state.owner = Owner("Default Owner")
    # Add a default pet so the user has something to click on
    st.session_state.owner.add_pet(Pet("Mochi", "Dog"))

st.title("🐾 PawPal+")
st.markdown("Your intelligent pet care assistant.")

st.divider()

# --- UI for Adding Tasks ---
st.subheader("Add a New Task")
col1, col2 = st.columns(2)

with col1:
    pet_names = [pet.name for pet in st.session_state.owner.pets]
    selected_pet_name = st.selectbox("Select Pet", pet_names) if pet_names else None
    task_title = st.text_input("Task Title", "Morning Walk")

with col2:
    due_time = st.time_input("Time").strftime("%H:%M")
    duration = st.number_input("Duration (mins)", min_value=1, value=20)
    frequency = st.selectbox("Frequency", ["Once", "Daily", "Weekly"])

if st.button("Schedule Task"):
    if selected_pet_name:
        # Find the pet object and add the task
        for pet in st.session_state.owner.pets:
            if pet.name == selected_pet_name:
                new_task = Task(task_title, due_time, duration, frequency)
                pet.add_task(new_task)
                st.success(f"Added '{task_title}' to {pet.name}'s schedule!")
    else:
        st.error("Please add a pet first.")

st.divider()

# --- UI for Generating Schedule ---
st.subheader("Today's Smart Schedule")

if st.button("Generate Schedule"):
    all_tasks = st.session_state.owner.get_all_tasks()
    
    if not all_tasks:
        st.info("No tasks scheduled yet.")
    else:
        # 1. Use Algorithm to Sort
        sorted_tasks = Scheduler.sort_tasks_by_time(all_tasks)
        
        # 2. Use Algorithm to Check Conflicts
        conflicts = Scheduler.check_conflicts(sorted_tasks)
        for conflict in conflicts:
            st.warning(conflict)
            
        # 3. Display Data
        schedule_data = []
        for p_name, task in sorted_tasks:
            schedule_data.append({
                "Time": task.due_time,
                "Pet": p_name,
                "Task": task.title,
                "Duration": f"{task.duration_mins}m",
                "Freq": task.frequency
            })
        st.table(schedule_data)