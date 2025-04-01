import tkinter as tk
from tkcalendar import Calendar

class CalendarTab:
    def __init__(self, parent):
        self.parent = parent  # Use the tab in task_tracker.py

        # Add the calendar in the tab
        self.calendar = Calendar(self.parent, selectmode="day", year=2025, month=3, day=31)
        self.calendar.pack(pady=20)

        # Button to take the selected date
        self.select_button = tk.Button(self.parent, text="Get Date", command=self.get_date)
        self.select_button.pack()

    def get_date(self):
        selected_date = self.calendar.get_date()
        print("Selected date:", selected_date)

