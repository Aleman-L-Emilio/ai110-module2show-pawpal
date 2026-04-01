from dataclasses import dataclass, field
from typing import List, Tuple
from datetime import datetime, timedelta

@dataclass
class Task:
    title: str
    due_time: str  # Format: "HH:MM"
    duration_mins: int
    frequency: str = "Once"  # "Once", "Daily", "Weekly"
    is_completed: bool = False

    def mark_complete(self):
        """Marks a task as complete and handles daily recurrence."""
        self.is_completed = True
        if self.frequency == "Daily":
            # In a real app, this would shift the date. For this scope, we just duplicate it.
            return Task(self.title, self.due_time, self.duration_mins, self.frequency, False)
        return None

@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Adds a new task to the pet's profile."""
        self.tasks.append(task)

@dataclass
class Owner:
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        """Registers a new pet to the owner."""
        self.pets.append(pet)

    def get_all_tasks(self) -> List[Tuple[str, Task]]:
        """Returns a list of tuples containing (pet_name, task) for all pets."""
        all_tasks = []
        for pet in self.pets:
            for task in pet.tasks:
                all_tasks.append((pet.name, task))
        return all_tasks

class Scheduler:
    """The brain of PawPal+ that handles sorting and algorithms."""
    
    @staticmethod
    def sort_tasks_by_time(tasks: List[Tuple[str, Task]]) -> List[Tuple[str, Task]]:
        """Sorts a list of (pet_name, task) tuples chronologically by due_time."""
        # Using a lambda function as the sort key based on the "HH:MM" string
        return sorted(tasks, key=lambda x: x[1].due_time)

    @staticmethod
    def check_conflicts(tasks: List[Tuple[str, Task]]) -> List[str]:
        """Detects if two tasks are scheduled at the exact same time."""
        warnings = []
        seen_times = {}
        for pet_name, task in tasks:
            if task.due_time in seen_times:
                warnings.append(f"Conflict Detected: '{task.title}' for {pet_name} is at the same time ({task.due_time}) as '{seen_times[task.due_time]}'!")
            else:
                seen_times[task.due_time] = task.title
        return warnings