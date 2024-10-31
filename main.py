from datetime import datetime
import tkinter as tk
from tkinter import ttk
import time


class App():
    def __init__(self):
        self.root = tk.Tk()
        
        # Time/Date Section
        self.clock_label = tk.Label(text="", foreground="white", background="black", font=("san-serif 72"))
        self.clock_label.pack()
        self.date_label = tk.Label(text="", foreground="white", background="black", font=("san-serif 32"))
        self.date_label.pack()
        self.root.geometry("700x350")
        self.root.configure(background="black")
        self.update_clock()
        
        
        self.seperator = ttk.Separator(self.root, orient="horizontal")
        self.seperator.pack(fill="x", pady="50")
        
        # Weather Section
        # TODO: Use OpenWeatherAPI
        self.weather_title = tk.Label(text="Current Weather", foreground="white", background="black", font=("san-serif 32"))
        self.weather_title.pack()
        self.current_temp = tk.Label(text="", foreground="white", background="black", font=("san-serif 48"))
        self.current_temp.pack()
        self.current_condition = tk.Label(text="", foreground="white", background="black", font=("san-serif 16"))
        self.current_condition.pack()
        self.humidity = tk.Label(text="", foreground="white", background="black", font=("san-serif 16"))
        self.humidity.pack()
        self.wind = tk.Label(text="", foreground="white", background="black", font=("san-serif 16"))
        self.wind.pack()
        self.weather_icon = tk.Label(text="", foreground="white", background="black", font=("san-serif 32"))
        self.weather_icon.pack()
        
        # Forecast Section
        self.today_forecast = tk.Frame()
        self.tomorow_forecast = tk.Frame()
        self.upcoming_forecast = tk.Frame()
        
        
        
        self.root.wm_attributes("-fullscreen", "True")
        self.root.mainloop()
        
    def update_clock(self):
        now = time.strftime("%H:%M %p")
        date = datetime.now()
        self.clock_label.config(text=now)
        self.date_label.config(text=date.strftime("%A %B %d, %Y"))
        self.root.after(1000, self.update_clock)
        
app=App()