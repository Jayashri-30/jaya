import tkinter as tk
import time

def update_time():
    current_time = time.strftime('%H:%M:%S')
    label.config(text=current_time)
    root.after(1000, update_time)  # update every second

root = tk.Tk()
root.title("Digital Clock")

label = tk.Label(root, font=('Helvetica', 48), fg='blue')
label.pack()

update_time()
root.mainloop()
