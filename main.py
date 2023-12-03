import tkinter as tk

root = tk.Tk()
height = 500
width = 500
root.title("First GUI")
# 0 is origin  from x-axis and 0 is origin for  y-axis
root.geometry(f"{height}x{width}+0+0")
root.iconbitmap(r"C:\Users\gtush\OneDrive\Desktop\GUI\firstGUI\please-give-me-1.ico")

text_box = tk.Text(root)
text_box.pack()


def click():
    text1 = "Hi " + text_box.get('1.0', tk.END)
    label.config(text=str(text1))


btn = tk.Button(root, command=click, text="Click")
btn.pack()
label = tk.Label(root)
label.pack()

# mainloop is used for staying the window when its run
root.mainloop()
