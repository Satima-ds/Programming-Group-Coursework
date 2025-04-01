import tkinter as tk

class HistoryTab:
    def __init__(self, parent):
        self.parent = parent

        # ----- Section "History" -----
        history_frame = tk.LabelFrame(self.parent, text="History", padx=10, pady=10)
        history_frame.pack(side=tk.LEFT, fill="both", expand=True, padx=10, pady=10)

        tk.Label(history_frame, text="Input Date:").grid(row=0, column=0, sticky="w")
        self.entry_date = tk.Entry(history_frame, width=10)
        self.entry_date.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(history_frame, text="Screen Time: 00:00").grid(row=1, column=0, columnspan=2, sticky="w")
        tk.Label(history_frame, text="Productivity Goal: 00:00").grid(row=2, column=0, columnspan=2, sticky="w")
        tk.Label(history_frame, text="Productivity Time: 00:00").grid(row=3, column=0, columnspan=2, sticky="w")
        tk.Label(history_frame, text="Productivity %: 00%").grid(row=4, column=0, columnspan=2, sticky="w")

        self.btn_load_history = tk.Button(history_frame, text="Load History", command=self.load_history)
        self.btn_load_history.grid(row=5, column=0, columnspan=2, pady=5)

        # ----- Section "Insights" -----
        insights_frame = tk.LabelFrame(self.parent, text="Insights", padx=10, pady=10)
        insights_frame.pack(side=tk.LEFT, fill="both", expand=True, padx=10, pady=10)

        self.insights_label = tk.Label(insights_frame, text=(
            "Your average productivity is up/down 00% this week\n"
            "while screen time is down/up 00%. Well done!/Oh no..."
        ))
        self.insights_label.pack(pady=10)

    def load_history(self):
        print("Charger l'historique pour la date:", self.entry_date.get(), "(à implémenter)")
