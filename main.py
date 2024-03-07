import tkinter as tk
from PIL import Image, ImageTk 
from window1 import Window1
from window2 import Window2
from window3 import Window3


def open_window1():
    window = tk.Toplevel()
    Window1(window)

def open_window2():
    window = tk.Toplevel()
    Window2(window)

def open_window3():
    window = tk.Toplevel()
    Window3(window)

def on_button_click(button_number):
    print(f"Button {button_number} clicked!")

def main():
    # Create the main window
    window = tk.Tk()
    window.title("Wrapping Application")

    window.geometry("1900x900")

    header_label = tk.Label(window, text="Present Wrapping Service", font=("Helvetica", 23))
    header_label.pack(pady=10)

    canvas = tk.Canvas(window, width=1700, height=600, bg="lightgray")
    canvas.pack()

    square_width = 400 
    square_height = 400


    # Square 1
    square1 = canvas.create_rectangle(50, 50, 50 + square_width, 50 + square_height, fill="#f0f0f0")
    label1 = tk.Label(window, text="Customer Page", font=("Helvetica", 14), bg="lightgray", fg="black")
    label1.place(x=280, y=435)

    # Load the Shopper Icon image
    image_path_Shopper = "img/ShopperIcon.png"
    image_Shopper = Image.open(image_path_Shopper)
    image_Shopper = image_Shopper.resize((250, 250))
    tk_image_Shopper = ImageTk.PhotoImage(image_Shopper)

    # Place the image in the center of the first square
    image_label_Shopper = tk.Label(window, image=tk_image_Shopper)
    image_label_Shopper.place(x=230, y=145)

    # Square 2
    square2 = canvas.create_rectangle(650, 50, 650 + square_width, 50 + square_height, fill="#f0f0f0")
    label2 = tk.Label(window, text="Staff Page", font=("Helvetica", 14), bg="lightgray", fg="black")
    label2.place(x=900, y=435)

    # Load the Staff Icon image
    image_path_Staff = "img/StaffIcon.png"
    image_Staff = Image.open(image_path_Staff)
    image_Staff = image_Staff.resize((250, 250))
    tk_image_Staff = ImageTk.PhotoImage(image_Staff)

    # Place the image in the center of the first square
    image_label_Staff = tk.Label(window, image=tk_image_Staff)
    image_label_Staff.place(x=830, y=145)

    # Square 3
    square3 = canvas.create_rectangle(1250, 50, 1250 + square_width, 50 + square_height, fill="#f0f0f0")
    label3 = tk.Label(window, text="Manager Page", font=("Helvetica", 14), bg="lightgray", fg="black")
    label3.place(x=1500, y=435)

    # Load the Manager Icon image
    image_path_Manager = "img/ManagerIcon.png"
    image_Manager = Image.open(image_path_Manager)
    image_Manager = image_Manager.resize((250, 250))
    tk_image_Manager = ImageTk.PhotoImage(image_Manager)

    # Place the image in the center of the first square
    image_label_Manager = tk.Label(window, image=tk_image_Manager)
    image_label_Manager.place(x=1435, y=145)

    # Buttons
    button1 = tk.Button(window, text="Button 1", command=open_window1, width=15, height=3, font=("Helvetica", 14))
    button1.place(x=260, y=520)

    button2 = tk.Button(window, text="Button 2", command=open_window2, width=15, height=3, font=("Helvetica", 14))
    button2.place(x=860, y=520)

    button3 = tk.Button(window, text="Button 3", command=open_window3, width=15, height=3, font=("Helvetica", 14))
    button3.place(x=1470, y=520)

    # Start the Tkinter event loop
    window.mainloop()

if __name__ == "__main__":
    main()
