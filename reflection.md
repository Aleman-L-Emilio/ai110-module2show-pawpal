# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**
My initial design included four core classes: `Task` (stores task details, duration, and frequency), `Pet` (stores name, species, and a list of Task objects), `Owner` (stores owner name and a list of Pet objects), and `Scheduler` (acts as the logic layer to manipulate and organize tasks).

**b. Design changes**
I initially planned to instantiate the `Scheduler` as an object that holds data, but I changed it to use `@staticmethod` functions instead. Since the Streamlit `st.session_state` and the `Owner` class already hold all the necessary state/data, the Scheduler just needed to be a functional "brain" that takes in data, processes it (sorting/conflict checking), and returns the results.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**
The scheduler primarily prioritizes chronological time to ensure tasks flow logically throughout the day. It also considers resource conflicts by flagging if an owner has accidentally double-booked themselves with two tasks at the exact same time.

**b. Tradeoffs**
For conflict detection, the system makes a tradeoff by only checking for exact `due_time` matches (e.g., two tasks starting exactly at "08:00") rather than calculating full overlapping durations (e.g., an 08:00 task taking 60 minutes overlapping with an 08:30 task). This keeps the algorithm simple, lightweight, and highly readable, which is reasonable for a lightweight personal pet care app where owners just need a gentle reminder about double-booking.

---

## 3. AI Collaboration

**a. How you used AI**
I used Copilot Chat extensively in the design phase to brainstorm Mermaid.js UML diagrams and scaffold the initial Python `@dataclass` structures. During the algorithmic phase, I used inline chat to help write the `lambda` function required to sort the string-based time formats ("HH:MM") chronologically.

**b. Judgment and verification**
When asking for a conflict detection algorithm, the AI initially suggested a highly complex approach using interval trees and external libraries. I rejected this because it was massive over-engineering for a simple pet app. Instead, I prompted it for a simpler dictionary-based approach (`seen_times`). I verified this simpler logic worked by writing a specific `pytest` function for it.

---

## 4. Testing and Verification

**a. What you tested**
I tested four core behaviors: task completion boolean toggling, pet task array appending, chronological sorting correctness, and duplicate-time conflict detection. These tests were important because they verify the "brain" of the app works perfectly in isolation, ensuring any UI bugs in Streamlit aren't caused by faulty core logic.

**b. Confidence**
I am highly confident (4/5 stars) in the core happy-path logic. If I had more time, the next edge cases I would test include handling invalid time string inputs (like "25:00"), negative duration integers, and what happens when an owner has zero pets but tries to generate a schedule.

---

## 5. Reflection

**a. What went well**
I am most satisfied with successfully bridging the pure Python backend logic with the Streamlit frontend. Understanding how to use `st.session_state` to keep my `Owner` object persistent across button clicks was a major breakthrough.

**b. What you would improve**
If I had another iteration, I would implement full duration-based overlap detection for scheduling conflicts, and I would connect the system to a simple SQLite database so the user's pets and tasks persist even if the Streamlit server restarts.

**c. Key takeaway**
I learned that being a "lead architect" with AI means strictly controlling complexity. AI will often write overly complex code if left unchecked; it is my job to evaluate the tradeoffs and enforce simple, readable, and testable designs.