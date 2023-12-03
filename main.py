import tkinter as tk
from tkinter import ttk

root = tk.Tk()
height = 500
width = 500
root.title("First GUI")
# 0 is origin  from x-axis and 0 is origin for  y-axis
root.geometry(f"{height}x{width}+0+0")
root.iconbitmap(r"C:\Users\gtush\OneDrive\Desktop\GUI\firstGUI\please-give-me-1.ico")

title = ttk.Label(root, text="Registration Form", foreground="black")
title.pack(pady=10)
main_frame = ttk.Frame(root)
main_frame.pack()

name_lab1 = ttk.Label(main_frame, text="Enter Name: ")
name_lab1.grid(column=0, row=0)

name_field1 = ttk.Entry(main_frame)
name_field1.grid(column=1, row=0)

email_lab1 = ttk.Label(main_frame, text="Enter Email: ")
email_lab1.grid(column=0, row=2, pady=20)

email_field = ttk.Entry(main_frame, show="*")
email_field.grid(column=1, row=2, pady=20)

gender_lab1 = ttk.Label(main_frame, text="Gender:")
gender_lab1.grid(column=0, row=3, pady=20)

gender = tk.StringVar()
radio_btn1 = ttk.Radiobutton(main_frame, text="Male", value="male", textvariable=gender)
radio_btn1.grid(column=1, row=3, pady=20)

radio_btn2 = ttk.Radiobutton(main_frame, text="Female", value="female", textvariable=gender)
radio_btn2.grid(column=2, row=3, pady=20)

# mainloop is used for staying the window when its run
root.mainloop()
