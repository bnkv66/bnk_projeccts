# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("My World")

# Create a canvas to draw on
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# Draw a rectangle to represent the world
canvas.create_rectangle(50, 50, 350, 350, fill="green")

# Add other elements to the world (e.g., objects, characters, etc.)

# Start the main event loop
window.mainloop()







