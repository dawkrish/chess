from .config import *
from tkinter import *
from ..database.get import get
from ..database.create import create_user

main_window=Tk()
main_window.geometry(f"{AUTH_WIDTH}x{AUTH_HEIGHT}") # window dimensions
main_window.title(f"{TITLE}")            # window title
main_window.config(background = "White")

heading = Label(main_window,
    text = "Welcome to Chess",
    font = ("Alef", 28, "bold"),
    fg = "Green",
    bg = "White")    
heading.pack()


def main_signin():
    window = Tk()
    window.geometry(f"{AUTH_WIDTH}x{AUTH_HEIGHT}") # window dimensions
    window.title(f"{TITLE}")            # window title
    window.config(background = "White") # window color

    form_heading = Label(window,
        text="Sign In",
        font=("Arial", 30),
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

def main_signup():
    window = Tk()
    window.geometry(f"{AUTH_WIDTH}x{AUTH_HEIGHT}") # window dimensions
    window.title(f"{TITLE}")            # window title
    window.config(background = "White") # window color

    form_heading = Label(window,
        text="Sign Up",
        font=("Arial", 30),
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


sign_in_button = Button(main_window,
    text = "Sign In",
    font = ("Arial",30),
    command = main_signin)
sign_in_button.pack()

sign_up_button = Button(main_window,
    text = "Sign Up",
    font = ("Arial",30),
    command = main_signup)
sign_up_button.pack()

main_window.mainloop()
