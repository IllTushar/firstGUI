import tkinter as tk

root = tk.Tk()
height = 500
width = 500
root.title("First GUI")
# 0 is origin  from x-axis and 0 is origin for  y-axis
root.geometry(f"{height}x{width}+0+0")
root.iconbitmap(r"C:\Users\gtush\OneDrive\Desktop\GUI\firstGUI\please-give-me-1.ico")

# Alignments=> pack ,grid ,place

label = tk.Label(root, text="Hi Tushar")
'''
label.pack(side="top")
label.grid(row=0, column=0)
label.place(x=20, y=50)
'''


def click():
    lbl = tk.Label(text="Thanks for press")
    lbl.pack()


btn = tk.Button(text="Click", command=click, fg="gold", bg="red")

btn.pack(padx=10, pady=20)
'''
btn = tk.Button(text="Click", command=click): In this line, 
you are assigning the click function (presumably defined elsewhere in your code) to the command parameter of the Button widget. 
This means that when the button is clicked, the click function will be executed.

btn = tk.Button(text="Click", command=click()): In this line, you are actually calling the click function and assigning its result to the command parameter. 
This means that the click function is executed immediately at the time of creating the button, and its return value is assigned to the command parameter.
If click returns a function, then that function will be assigned to the command.
'''

# mainloop is used for staying the window when its run
root.mainloop()
