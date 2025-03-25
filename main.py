import tkinter as tk
from tkinter import messagebox
import json
import time

# Initialize main window
root = tk.Tk()
root.title("Daily Task Tracker")
root.geometry("500x600")

tasks = []
current_task_index = None
start_time = None

# Function to add task
def add_task():
    task_name = task_entry.get()
    if task_name:
        tasks.append({"name": task_name, "status": "Incomplete", "time": 0, "in_process": False})
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task name cannot be empty!")

# Update task list display
def update_task_list():
    task_listbox.delete(0, tk.END)
    for idx, task in enumerate(tasks):
        if task.get('in_process', False):
            time_display = "in process"
        else:
            time_spent = task.get('time', 0)
            mins, secs = divmod(int(time_spent), 60)
            time_display = f"Time: {mins}m {secs}s"
        task_listbox.insert(tk.END, f"{idx+1}. {task['name']} - {task['status']} - {time_display}")

# Toggle task status
def toggle_status():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]['status'] = "Complete" if tasks[index]['status'] == "Incomplete" else "Incomplete"
        update_task_list()
    else:
        messagebox.showwarning("Warning", "Select a task first!")

# Start timing
def start_timing():
    global current_task_index, start_time
    selected = task_listbox.curselection()
    if selected:
        current_task_index = selected[0]
        start_time = time.time()
        tasks[current_task_index]['in_process'] = True
        update_task_list()
        messagebox.showinfo("Timing", f"Started timing task: {tasks[current_task_index]['name']}")
    else:
        messagebox.showwarning("Warning", "Select a task first!")

# Stop timing
def stop_timing():
    global current_task_index, start_time
    if current_task_index is not None and start_time is not None:
        elapsed = time.time() - start_time
        tasks[current_task_index]['time'] += elapsed
        tasks[current_task_index]['in_process'] = False
        update_task_list()
        messagebox.showinfo("Timing", f"Stopped timing. Elapsed: {elapsed//60:.0f} min {elapsed%60:.0f} sec.")
        current_task_index = None
        start_time = None
    else:
        messagebox.showwarning("Warning", "No task is currently being timed!")

# Save tasks to file
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

# Load tasks from file
def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            for task in tasks:
                task.setdefault('in_process', False)
                task.setdefault('time', 0)
        update_task_list()
    except FileNotFoundError:
        tasks = []

# Task entry
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Add task button
add_task_button = tk.Button(root, text="Add Task", command=add_task)
add_task_button.pack()

# List of tasks
task_listbox = tk.Listbox(root, width=60, height=15)
task_listbox.pack(pady=20)

# Add toggle button
toggle_button = tk.Button(root, text="Toggle Complete/Incomplete", command=toggle_status)
toggle_button.pack(pady=5)

# Add timing buttons
start_timer_button = tk.Button(root, text="Start Task", command=start_timing)
start_timer_button.pack(pady=5)

stop_timer_button = tk.Button(root, text="Stop Task", command=stop_timing)
stop_timer_button.pack(pady=5)

# Load tasks at the beginning
load_tasks()

# Ensure tasks are saved when the application closes
root.protocol("WM_DELETE_WINDOW", lambda: (save_tasks(), root.destroy()))

root.mainloop()