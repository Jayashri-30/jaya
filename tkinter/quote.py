import tkinter as tk
import random

quotes = [
    "Believe in yourself.",
    "Keep pushing forward.",
    "Stay positive.",
    "You can do it!",
    "Never give up!"
]

def show_quote():
    quote_label.config(text=random.choice(quotes))

root = tk.Tk()
root.title("Quote Generator")

tk.Button(root, text="Get Quote", command=show_quote).pack(pady=10)
quote_label = tk.Label(root, text="", wraplength=300, font=('Arial', 14))
quote_label.pack(pady=10)

root.mainloop()
