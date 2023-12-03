import tkinter as tk

root = tk.Tk()
height = 500
width = 500
root.title("First GUI")
# 0 is origin  from x-axis and 0 is origin for  y-axis
root.geometry(f"{height}x{width}+0+0")
root.iconbitmap(r"C:\Users\gtush\OneDrive\Desktop\GUI\firstGUI\please-give-me-1.ico")


def click():
    print(gender.get())


gender = tk.StringVar()
radio_btn1 = tk.Radiobutton(root, variable=gender, value="male", text="Male")

radio_btn1.place(x=100, y=50)
gender.set("Male")

radio_btn1 = tk.Radiobutton(root, variable=gender, value="female", text="Female")
radio_btn1.place(x=200, y=50)

btn = tk.Button(root, command=click, text="Click")
btn.place(x=150, y=150)
label = tk.Label(root)
label.pack()

# mainloop is used for staying the window when its run
root.mainloop()
