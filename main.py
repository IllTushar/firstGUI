import tkinter as tk
from tkinter import ttk

root = tk.Tk()
height = 500
width = 500
root.title("First GUI")
# 0 is origin  from x-axis and 0 is origin for  y-axis
root.geometry(f"{height}x{width}+0+0")
root.iconbitmap(r"C:\Users\gtush\OneDrive\Desktop\GUI\firstGUI\please-give-me-1.ico")


def action():
    print(mycombo.get())


mycombo = ttk.Combobox(root, font='arial', state='readonly', justify='center')
mycombo['value'] = ('Select the Value', "Java", "Python", "HTML")
mycombo.set(mycombo['value'][0])
mycombo.pack()
btn_click = ttk.Button(root, command=action, text="click")
btn_click.pack()

# mainloop is used for staying the window when its run
root.mainloop()
