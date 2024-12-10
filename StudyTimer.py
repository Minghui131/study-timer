import tkinter as tk
from tkinter import messagebox
import time
import threading

class StudyTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Study Timer")

        self.study_time = tk.IntVar(value=25)  # Study time in minutes
        self.break_time = tk.IntVar(value=5)  # Break time in minutes
        self.is_running = False

        # UI Components
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Study Timer").grid(row=0, column=1, pady=10)

        tk.Label(self.root, text="Study Time (minutes):").grid(row=1, column=0, pady=5)
        tk.Entry(self.root, textvariable=self.study_time).grid(row=1, column=1, pady=5)

        tk.Label(self.root, text="Break Time (minutes):").grid(row=2, column=0, pady=5)
        tk.Entry(self.root, textvariable=self.break_time).grid(row=2, column=1, pady=5)

        self.start_button = tk.Button(self.root, text="Start Timer", command=self.start_timer)
        self.start_button.grid(row=3, column=0, pady=10)

        self.stop_button = tk.Button(self.root, text="Stop Timer", command=self.stop_timer)
        self.stop_button.grid(row=3, column=1, pady=10)

        self.timer_label = tk.Label(self.root, text="Timer: 00:00", font=("Helvetica", 16))
        self.timer_label.grid(row=4, column=0, columnspan=2, pady=10)

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            study_seconds = self.study_time.get() * 60
            break_seconds = self.break_time.get() * 60
            threading.Thread(target=self.run_timer, args=(study_seconds, break_seconds)).start()

    def stop_timer(self):
        self.is_running = False

    def run_timer(self, study_seconds, break_seconds):
        while self.is_running:
            self.countdown(study_seconds, "Study Time")
            if not self.is_running:
                break
            messagebox.showinfo("Break Time", "Time for a break! Stretch or take a deep breath.")
            self.countdown(break_seconds, "Break Time")
            if not self.is_running:
                break

    def countdown(self, total_seconds, mode):
        for remaining in range(total_seconds, -1, -1):
            if not self.is_running:
                break
            mins, secs = divmod(remaining, 60)
            self.timer_label.config(text=f"{mode}: {mins:02}:{secs:02}")
            time.sleep(1)
        self.timer_label.config(text="Timer: 00:00")

# Main Application
if __name__ == "__main__":
    root = tk.Tk()
    app = StudyTimer(root)
    root.mainloop()