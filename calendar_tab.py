import tkinter as tk
from tkcalendar import Calendar

class CalendarTab:
    def __init__(self, parent):
        self.parent = parent  # Utilise l'onglet donné par TaskTrackerApp

        # Ajout du calendrier dans l'onglet
        self.calendar = Calendar(self.parent, selectmode="day", year=2025, month=3, day=31)
        self.calendar.pack(pady=20)

        # Bouton pour récupérer la date sélectionnée
        self.select_button = tk.Button(self.parent, text="Get Date", command=self.get_date)
        self.select_button.pack()

    def get_date(self):
        selected_date = self.calendar.get_date()
        print("Selected date:", selected_date)

