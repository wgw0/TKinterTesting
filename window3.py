import tkinter as tk

class Window3:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel(parent)
        self.window.title("Window 3")

        # Add content to Window 3
        label = tk.Label(self.window, text="This is Window 3")
        label.pack(padx=20, pady=20)
