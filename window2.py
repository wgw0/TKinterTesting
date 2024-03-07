import tkinter as tk

class Window2:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel(parent)
        self.window.title("Window 2")

        # Add content to Window 2
        label = tk.Label(self.window, text="This is Window 2")
        label.pack(padx=20, pady=20)
