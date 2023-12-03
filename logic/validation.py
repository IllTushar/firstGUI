import tkinter as tk
from tkinter import ttk


class RegistrationForm:
    def __init__(self, root):
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        self.title = ttk.Label(self.root, text="Registration Form", foreground="black")
        self.title.pack(pady=10)

        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack()

        # Validation
        validate_email = self.root.register(self.validate_email)
        validate_name = self.root.register(self.validate_name)

        self.name_lab1 = ttk.Label(self.main_frame, text="Enter Name: ")
        self.name_lab1.grid(column=0, row=0)

        self.name_field1 = ttk.Entry(self.main_frame, validate="key", validatecommand=(validate_name, "%P"))
        self.name_field1.grid(column=1, row=0)

        self.email_lab1 = ttk.Label(self.main_frame, text="Enter Email: ")
        self.email_lab1.grid(column=0, row=2, pady=20)

        self.email_field = ttk.Entry(self.main_frame, validate="key", validatecommand=(validate_email, "%P"))
        self.email_field.grid(column=1, row=2, pady=20)

        self.gender_lab1 = ttk.Label(self.main_frame, text="Gender")
        self.gender_lab1.grid(column=0, row=3, pady=10)

        self.gender = tk.StringVar()
        self.radio_btn1 = ttk.Radiobutton(self.main_frame, text="Male", value="male", variable=self.gender)
        self.radio_btn1.grid(column=1, row=3, pady=10)

        self.radio_btn2 = ttk.Radiobutton(self.main_frame, text="Female", value="female", variable=self.gender)
        self.radio_btn2.grid(column=2, row=3, pady=10)

        style = ttk.Style()
        style.configure("TButton", background="blue", foreground="black")
        self.save = ttk.Button(self.main_frame, text="Save", style="TButton", command=self.save_data)
        self.save.grid(row=4, pady=10, columnspan=2)

    def validate_name(self, name):
        # Your validation logic for the name field
        return len(name) <= 20  # For example, require a name of maximum 20 characters

    def validate_email(self, email):
        # Your validation logic for the email field
        return '@' in email  # For example, require the presence of '@' in the email

    def save_data(self):
        name = self.name_field1.get()
        email = self.email_field.get()
        g_gender = self.gender.get()
        if not name:
            print("Enter Name")
        elif not email:
            print("Enter Email")
        elif not g_gender:
            print("Check the checkbox")
        else:
            print("Data Add Successful")
