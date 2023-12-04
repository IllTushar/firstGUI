import tkinter as tk

root = tk.Tk()
height = 500
width = 500
root.title("First GUI")
# 0 is origin  from x-axis and 0 is origin for  y-axis
root.geometry(f"{height}x{width}+0+0")
root.iconbitmap(r"C:\Users\gtush\OneDrive\Desktop\GUI\firstGUI\please-give-me-1.ico")


def printStat():
    print("Successful")


menus = tk.Menu(root)
Student = tk.Menu(menus, tearoff=0)
Student.add_cascade(label="New File", command=printStat)
Student.add_cascade(label="Settings", command=printStat)
menus.add_cascade(label="File", menu=Student)
root.config(menu=menus)
# mainloop is used for staying the window when its run
root.mainloop()
