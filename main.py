import tkinter as tk
from logic.validation import RegistrationForm
if __name__ == "__main__":
    root = tk.Tk()
    height = 500
    width = 500
    root.title("First GUI")
    root.geometry(f"{height}x{width}+0+0")

    app = RegistrationForm(root)

    root.mainloop()
