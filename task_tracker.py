import tkinter as tk
from tkinter import messagebox
import time
from task_manager import TaskManager
from tkinter import ttk
from calendar_tab import CalendarTab

class TaskTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Daily Task Tracker")
        self.root.geometry("600x650")

        self.task_manager = TaskManager()
        self.current_task_index = None
        self.start_time = None

        #----------- Notebook (Tabs managing) -----------
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill="both")

        # Tasks tab
        self.tab_tasks = tk.Frame(self.notebook)
        self.notebook.add(self.tab_tasks, text="Tasks")

        # Calendar tab
        self.tab_calendar = tk.Frame(self.notebook)
        self.notebook.add(self.tab_calendar, text="Calendar")

        self.calendar_tab = CalendarTab(self.tab_calendar)

        #"Input ~ Daily total" tab
        
        #"Progress" tab
        
        #"History ~ Insight" tab

        
        #----------- Interface for the tasks in the tasks tab -----------
        tk.Label(self.tab_tasks, text="New Task:").pack()
        self.task_entry = tk.Entry(self.tab_tasks, width=40)
        self.task_entry.pack(pady=10)

        add_task_button = tk.Button(self.tab_tasks, text="Add Task", command=self.add_task)
        add_task_button.pack()

        self.task_listbox = tk.Listbox(self.tab_tasks, width=60, height=15)
        self.task_listbox.pack(pady=20)

        toggle_button = tk.Button(self.tab_tasks, text="Toggle Complete/Incomplete", command=self.toggle_status)
        toggle_button.pack(pady=5)

        start_timer_button = tk.Button(self.tab_tasks, text="Start Task", command=self.start_timing)
        start_timer_button.pack(pady=5)

        stop_timer_button = tk.Button(self.tab_tasks, text="Stop Task", command=self.stop_timing)
        stop_timer_button.pack(pady=5)

        remove_task_button = tk.Button(self.tab_tasks, text="Remove Task", command=self.remove_task)
        remove_task_button.pack(pady=5)

        self.update_task_list()
        self.root.protocol("WM_DELETE_WINDOW", self.save_and_exit)

    def update_task_list(self):
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

            if task['status'] == 'Complete':
                self.task_listbox.itemconfig(idx, {'fg': 'green'})

    def add_task(self):
        task_name = self.task_entry.get()
        if task_name:
            self.task_manager.add_task(task_name)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task name cannot be empty!")

    def remove_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.task_manager.remove_task(index)
            self.update_task_list()
        else:
            messagebox.showwarning("Warning", "Select a task first!")

    def toggle_status(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.task_manager.toggle_status(index)
            self.update_task_list()
        else:
            messagebox.showwarning("Warning", "Select a task first!")

    def start_timing(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            if self.current_task_index is not None:
                self.stop_timing()
            self.current_task_index = index
            self.start_time = time.time()
            self.task_manager.start_task(index)
            self.update_task_list()
            messagebox.showinfo("Timing", f"Started timing task: {self.task_manager.get_task(index)['name']}")
        else:
            messagebox.showwarning("Warning", "Select a task first!")

    def stop_timing(self):
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
        self.task_manager.save_tasks()
        self.root.destroy()

#--------------Input  and daily total section
    #~~~~Input~~~~

# Screen time: 
#Productivity Goal:
#Productivity time:


#producivity times ---->  <Go>  <Stop>


    #~~~~Daily total~~~~

#Screen time: 00:00   <Clear>
#Productivity time: 00:00 <Clear>

#--------------------------------------------------------



#--------------Progress section

#Screen Time: <WW> <MM> <YYYY>

#Plot @#?!£.?/

#Productivity: <WW> <MM> <YYYY>

#plot @#?!£.?/


#------------------------------------------------------------------------



#---------------History and Insight section

       #~~~~History~~~~~

#Input date: 

#Screen time: 00:00
#Productivity Goal: 00:00
#Productivity time: 00:00

#Producivity %: 00%

       #~~~~~Insights~~~~~

#f"Your average productivity is up/down 00% this week 
# while screen time is down/up 00%. Well done !/ Oh no..."

#-------------------------------------------------------------------------



if __name__ == "__main__":
    root = tk.Tk()
    app = TaskTrackerApp(root)
    root.mainloop()
