import tkinter as tk

class ProgressTab:
    def __init__(self, parent):
        self.parent = parent

        # ----- Section "Screen Time" -----
        screen_time_frame = tk.LabelFrame(self.parent, text="Screen Time", padx=10, pady=10)
        screen_time_frame.pack(side=tk.LEFT, fill="both", expand=True, padx=10, pady=10)

        tk.Label(screen_time_frame, text="View by:").pack()
        self.btn_week_st = tk.Button(screen_time_frame, text="Week", command=lambda: self.show_screen_time("week"))
        self.btn_week_st.pack(side=tk.LEFT, padx=5)
        self.btn_month_st = tk.Button(screen_time_frame, text="Month", command=lambda: self.show_screen_time("month"))
        self.btn_month_st.pack(side=tk.LEFT, padx=5)
        self.btn_year_st = tk.Button(screen_time_frame, text="Year", command=lambda: self.show_screen_time("year"))
        self.btn_year_st.pack(side=tk.LEFT, padx=5)

        # ----- Section "Productivity" -----
        productivity_frame = tk.LabelFrame(self.parent, text="Productivity", padx=10, pady=10)
        productivity_frame.pack(side=tk.LEFT, fill="both", expand=True, padx=10, pady=10)

        tk.Label(productivity_frame, text="View by:").pack()
        self.btn_week_prod = tk.Button(productivity_frame, text="Week", command=lambda: self.show_productivity("week"))
        self.btn_week_prod.pack(side=tk.LEFT, padx=5)
        self.btn_month_prod = tk.Button(productivity_frame, text="Month", command=lambda: self.show_productivity("month"))
        self.btn_month_prod.pack(side=tk.LEFT, padx=5)
        self.btn_year_prod = tk.Button(productivity_frame, text="Year", command=lambda: self.show_productivity("year"))
        self.btn_year_prod.pack(side=tk.LEFT, padx=5)

    def show_screen_time(self, period):
        print(f"Display the screen time evolution for: {period} (To be implemented)")

    def show_productivity(self, period):
        print(f"Display the productivity time for: {period} (To be implemented)")
