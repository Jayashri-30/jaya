import tkinter as tk

def paint(event):
    x1, y1 = (event.x - 2), (event.y - 2)
    x2, y2 = (event.x + 2), (event.y + 2)
    canvas.create_oval(x1, y1, x2, y2, fill="black")

root = tk.Tk()
root.title("Simple Paint App")

canvas = tk.Canvas(root, bg="white", width=500, height=500)
canvas.pack()
canvas.bind("<B1-Motion>", paint)

root.mainloop()
