import tkinter as tk
from tkinter import messagebox

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        self.root.geometry("300x400")
        self.root.configure(bg="light grey")

        self.time_left = 0
        self.running = False
        self.paused = False

        self.label = tk.Label(root, text="00:00:00", font=("Helvetica", 48), bg="light grey")
        self.label.pack(pady=20)

        self.entry = tk.Entry(root, font=("Helvetica", 24))
        self.entry.pack(pady=10)

        self.set_button = tk.Button(root, text="Set Time", command=self.set_time, bg="light blue", fg="black", font=("Helvetica", 16), width=10)
        self.set_button.pack(pady=5)

        self.start_button = tk.Button(root, text="Start", command=self.start, bg="light green", fg="black", font=("Helvetica", 16), width=10)
        self.start_button.pack(pady=5)

        self.pause_button = tk.Button(root, text="Pause", command=self.pause, bg="yellow", fg="black", font=("Helvetica", 16), width=10)
        self.pause_button.pack(pady=5)

        self.resume_button = tk.Button(root, text="Resume", command=self.resume, bg="orange", fg="black", font=("Helvetica", 16), width=10)
        self.resume_button.pack(pady=5)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset, bg="red", fg="white", font=("Helvetica", 16), width=10)
        self.reset_button.pack(pady=5)

        self.update_timer()

    def set_time(self):
        try:
            time_str = self.entry.get()
            h, m, s = map(int, time_str.split(":"))
            self.time_left = h * 3600 + m * 60 + s
            self.label.config(text=f"{h:02}:{m:02}:{s:02}")
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter time in HH:MM:SS format")

    def start(self):
        if not self.running and self.time_left > 0:
            self.running = True
            self.paused = False
            self.countdown()

    def pause(self):
        if self.running and not self.paused:
            self.paused = True

    def resume(self):
        if self.running and self.paused:
            self.paused = False
            self.countdown()

    def reset(self):
        self.running = False
        self.paused = False
        self.time_left = 0
        self.label.config(text="00:00:00")

    def countdown(self):
        if self.running and not self.paused:
            if self.time_left > 0:
                self.time_left -= 1
                minutes, seconds = divmod(self.time_left, 60)
                hours, minutes = divmod(minutes, 60)
                self.label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
                self.root.after(1000, self.countdown)
            else:
                self.running = False
                messagebox.showinfo("Time's up", "The countdown has finished")

    def update_timer(self):
        if self.running and not self.paused:
            minutes, seconds = divmod(self.time_left, 60)
            hours, minutes = divmod(minutes, 60)
            self.label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
        self.root.after(100, self.update_timer)

root = tk.Tk
app = CountdownTimer(root)
root.mainloop()i