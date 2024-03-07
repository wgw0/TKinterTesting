import tkinter as tk

class Window1:
    def __init__(self):
        self.window = tk.Tk()  # Create a new Tk() instance for Window1
        self.window.title("Window 1")

        # Add content to Window 1
        label = tk.Label(self.window, text="This is Window 1")
        label.pack(padx=20, pady=20)

        # You can add more content or configure the window as needed

    def run(self):
        self.window.mainloop()

# Example usage:
if __name__ == "__main__":
    window1 = Window1()
    window1.run()
