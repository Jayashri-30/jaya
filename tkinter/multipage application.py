import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Multi-Page App")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)

notebook.add(frame1, text='Home')
notebook.add(frame2, text='Settings')

tk.Label(frame1, text="Welcome to Home Page").pack(pady=20)
tk.Label(frame2, text="Settings Page").pack(pady=20)

root.mainloop()
