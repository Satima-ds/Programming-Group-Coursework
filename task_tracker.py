import tkinter as tk
from tkinter import messagebox
import time
from task_manager import TaskManager

class TaskTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Daily Task Tracker")
        self.root.geometry("500x650")

        self.task_manager = TaskManager()
        self.current_task_index = None
        self.start_time = None

        # Entry to add the tasks
        tk.Label(root, text="New Task:").pack()
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        # Add task button
        add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_task_button.pack()

        # List of tasks
        self.task_listbox = tk.Listbox(root, width=60, height=15)
        self.task_listbox.pack(pady=20)

        # Button to modify the state of the task (Finished/Unfinished)
        toggle_button = tk.Button(root, text="Toggle Complete/Incomplete", command=self.toggle_status)
        toggle_button.pack(pady=5)

        # Chrono buttons
        start_timer_button = tk.Button(root, text="Start Task", command=self.start_timing)
        start_timer_button.pack(pady=5)

        stop_timer_button = tk.Button(root, text="Stop Task", command=self.stop_timing)
        stop_timer_button.pack(pady=5)

        # Delete task button
        remove_task_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        remove_task_button.pack(pady=5)

        self.update_task_list()

        # Save the tasks when the app is closed
        self.root.protocol("WM_DELETE_WINDOW", self.save_and_exit)

    def update_task_list(self):
        """Update de display of the tasks in the lists."""
        self.task_listbox.delete(0, tk.END)
        for idx, task in enumerate(self.task_manager.get_tasks()):
            if task.get('in_process', False):
                time_display = "in process"
            else:
                time_spent = task.get('time', 0)
                mins, secs = divmod(int(time_spent), 60)
                time_display = f"Time: {mins}m {secs}s"

            status_display = f"{idx+1}. {task['name']} - {task['status']} - {time_display}"
            self.task_listbox.insert(tk.END, status_display)

            # Différencier visuellement les tâches complètes
            if task['status'] == 'Complete':
                self.task_listbox.itemconfig(idx, {'fg': 'green'})

    def add_task(self):
        """Add a new task"""
        task_name = self.task_entry.get()
        if task_name:
            self.task_manager.add_task(task_name)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task name cannot be empty!")

    def remove_task(self):
        """Delete the selectioned task"""
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.task_manager.remove_task(index)
            self.update_task_list()
        else:
            messagebox.showwarning("Warning", "Select a task first!")

    def toggle_status(self):
        """Modifie the state of the selectioned task."""
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.task_manager.toggle_status(index)
            self.update_task_list()
        else:
            messagebox.showwarning("Warning", "Select a task first!")

    def start_timing(self):
        """Start the chrono for the selectioned task."""
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            if self.current_task_index is not None:
                self.stop_timing()  # Arrêter le chronomètre précédent
            self.current_task_index = index
            self.start_time = time.time()
            self.task_manager.start_task(index)
            self.update_task_list()
            messagebox.showinfo("Timing", f"Started timing task: {self.task_manager.get_task(index)['name']}")
        else:
            messagebox.showwarning("Warning", "Select a task first!")

    def stop_timing(self):
        """Stop the chrono and display the time"""
        if self.current_task_index is not None and self.start_time is not None:
            elapsed_time = time.time() - self.start_time
            self.task_manager.stop_task(self.current_task_index, elapsed_time)
            self.update_task_list()
            messagebox.showinfo("Timing", f"Stopped timing. Elapsed: {elapsed_time//60:.0f} min {elapsed_time%60:.0f} sec.")
            self.current_task_index = None
            self.start_time = None
        else:
            messagebox.showwarning("Warning", "No task is currently being timed!")

    def save_and_exit(self):
        """Save the task."""
        self.task_manager.save_tasks()
        self.root.destroy()

