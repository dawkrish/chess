from .config import *
from tkinter import *
from ..database.get import get
from ..database.create import create_user

def main_signup():
    window = Tk()
    window.geometry(f"{AUTH_WIDTH}x{AUTH_HEIGHT}") # window dimensions
    window.title(f"{TITLE}")            # window title
    window.config(background = "White") # window color

    form_heading = Label(window,
        text="Sign Up",
        font=("Arial", 28),
        fg="Black",
        bg="White")
    form_heading.pack()

    username_label = Label(window,
        text = "Enter your username",
        font = ("Arial",20),
        bg = "White")
    username_label.pack()

    username_entry = Entry(window,
        font = (("arial", 20)))
    username_entry.pack()

    password_label = Label(window,
        text = "Enter your password!",
        font = ("Arial",20),
        bg = "White")
    password_label.pack()

    password_entry = Entry(window,
        font = ("arial",20),
        show = "*")
    password_entry.pack()

    def signup_fn():
        username = username_entry.get()
        res = get("users", f"username = '{username}'")
        if len(res) != 0:
            raise ValueError("User already exists")
        password = password_entry.get()
        if len(password) < 8:
            raise ValueError("Password is too short (should be >= 8)!")
        create_user(username, password)
        print("Done")
        window.destroy()

    signup_button = Button(window,
        text = "Submit",
        command = signup_fn)

    signup_button.pack()

    window.mainloop()
