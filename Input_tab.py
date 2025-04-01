import tkinter as tk

class InputDailyTab:
    def __init__(self, parent):
        self.parent = parent

        # ----- Section "Input" -----
        input_frame = tk.LabelFrame(self.parent, text="Input", padx=10, pady=10)
        input_frame.pack(side=tk.TOP, fill="x", padx=10, pady=5)

        # Screen Time
        tk.Label(input_frame, text="Screen Time:").grid(row=0, column=0, sticky="w")
        self.entry_screen_time = tk.Entry(input_frame, width=10)
        self.entry_screen_time.grid(row=0, column=1, padx=5, pady=5)

        # Productivity Goal
        tk.Label(input_frame, text="Productivity Goal:").grid(row=1, column=0, sticky="w")
        self.entry_productivity_goal = tk.Entry(input_frame, width=10)
        self.entry_productivity_goal.grid(row=1, column=1, padx=5, pady=5)

        # Productivity Time
        tk.Label(input_frame, text="Productivity Time:").grid(row=2, column=0, sticky="w")
        self.entry_productivity_time = tk.Entry(input_frame, width=10)
        self.entry_productivity_time.grid(row=2, column=1, padx=5, pady=5)

        # Boutons du timer
        timer_frame = tk.Frame(input_frame)
        timer_frame.grid(row=3, column=0, columnspan=2, pady=5)
        self.btn_go = tk.Button(timer_frame, text="Go", command=self.start_productivity_timer)
        self.btn_go.pack(side=tk.LEFT, padx=5)
        self.btn_stop = tk.Button(timer_frame, text="Stop", command=self.stop_productivity_timer)
        self.btn_stop.pack(side=tk.LEFT, padx=5)

        # ----- Section "Daily Total" -----
        daily_total_frame = tk.LabelFrame(self.parent, text="Daily Total", padx=10, pady=10)
        daily_total_frame.pack(side=tk.TOP, fill="x", padx=10, pady=5)

        # Daily Screen Time
        tk.Label(daily_total_frame, text="Screen Time: 00:00").grid(row=0, column=0, sticky="w")
        self.btn_clear_screen = tk.Button(daily_total_frame, text="Clear", command=self.clear_screen_time)
        self.btn_clear_screen.grid(row=0, column=1, padx=5, pady=5)

        # Daily Productivity Time
        tk.Label(daily_total_frame, text="Productivity Time: 00:00").grid(row=1, column=0, sticky="w")
        self.btn_clear_productivity = tk.Button(daily_total_frame, text="Clear", command=self.clear_productivity_time)
        self.btn_clear_productivity.grid(row=1, column=1, padx=5, pady=5)

    def start_productivity_timer(self):
        # Logique pour démarrer le chronomètre de productivité
        print("Démarrage du chronomètre de productivité... (à implémenter)")

    def stop_productivity_timer(self):
        # Logique pour arrêter le chronomètre de productivité
        print("Arrêt du chronomètre de productivité... (à implémenter)")

    def clear_screen_time(self):
        # Logique pour réinitialiser le temps d'écran journalier
        print("Réinitialisation du temps d'écran journalier... (à implémenter)")

    def clear_productivity_time(self):
        # Logique pour réinitialiser le temps de productivité journalier
        print("Réinitialisation du temps de productivité journalier... (à implémenter)")
