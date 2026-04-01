from pawpal_system import Owner, Pet, Task, Scheduler

# 1. Create Data
jordan = Owner("Jordan")
mochi = Pet("Mochi", "Dog")
luna = Pet("Luna", "Cat")

jordan.add_pet(mochi)
jordan.add_pet(luna)

mochi.add_task(Task("Morning Walk", "08:00", 30, "Daily"))
mochi.add_task(Task("Dinner", "18:00", 15, "Daily"))
luna.add_task(Task("Brush Fur", "08:00", 10, "Weekly")) # Conflict!

# 2. Retrieve and Sort
all_tasks = jordan.get_all_tasks()
sorted_tasks = Scheduler.sort_tasks_by_time(all_tasks)
conflicts = Scheduler.check_conflicts(sorted_tasks)

# 3. Print Results
print(f"--- {jordan.name}'s Daily Schedule ---")
for pet_name, task in sorted_tasks:
    status = "[x]" if task.is_completed else "[ ]"
    print(f"{task.due_time} | {status} {pet_name}: {task.title} ({task.duration_mins}m)")

if conflicts:
    print("\n⚠️ WARNINGS:")
    for w in conflicts:
        print(w)