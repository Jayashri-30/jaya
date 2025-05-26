import tkinter as tk

def start_timer():
    try:
        count = int(entry.get())
        countdown(count)
    except ValueError:
        label.config(text="Enter a valid number")

def countdown(time_left):
    if time_left >= 0:
        label.config(text=f"Time left: {time_left}s")
        root.after(1000, countdown, time_left - 1)
    else:
        label.config(text="Time's up!")

root = tk.Tk()
root.title("Countdown Timer")

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Start", command=start_timer).pack(pady=5)
label = tk.Label(root, text="")
label.pack()

root.mainloop()
