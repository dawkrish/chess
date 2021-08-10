from tkinter import *
from .config import *
from ..database.get import get

def main_signin():
    window = Tk()
    window.geometry(f"{AUTH_WIDTH}x{AUTH_HEIGHT}") # window dimensions
    window.title(f"{TITLE}")            # window title
    window.config(background = "White") # window color

    form_heading = Label(window,
        text="Sign In",
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

    def signin_fn():
        username = username_entry.get()
        password = password_entry.get()
        res = get("users", f"username = '{username}'")
        if len(res) != 1:
            raise ValueError("Invalid User")
        user_details = res[0]
        if user_details[1] != password:
            raise ValueError("Invalid Password")
        print("Done")
        window.destroy()

    signin_button = Button(window,
        text = "Submit",
        command = signin_fn)

    signin_button.pack()

    window.mainloop()