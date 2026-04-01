from pawpal_system import Task, Pet, Scheduler

def test_task_completion():
    t = Task("Walk", "08:00", 30)
    assert t.is_completed == False
    t.mark_complete()
    assert t.is_completed == True

def test_pet_task_addition():
    p = Pet("Mochi", "Dog")
    p.add_task(Task("Walk", "08:00", 30))
    assert len(p.tasks) == 1

def test_sorting_logic():
    t1 = ("Mochi", Task("Dinner", "18:00", 30))
    t2 = ("Mochi", Task("Breakfast", "07:00", 30))
    sorted_tasks = Scheduler.sort_tasks_by_time([t1, t2])
    # Breakfast should come before Dinner
    assert sorted_tasks[0][1].title == "Breakfast"

def test_conflict_detection():
    t1 = ("Mochi", Task("Walk", "08:00", 30))
    t2 = ("Luna", Task("Vet", "08:00", 60))
    warnings = Scheduler.check_conflicts([t1, t2])
    assert len(warnings) == 1
    assert "Conflict Detected" in warnings[0]