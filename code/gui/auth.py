from .config import *
from .signin import *
from .signup import *
from tkinter import *
from ..database.get import get
from ..database.create import create_user


main_window=Tk()
main_window.geometry(f"{AUTH_WIDTH}x{AUTH_HEIGHT}") # window dimensions
main_window.title(f"{TITLE}")            # window title
main_window.config(background = "White")

photo = PhotoImage(file="chess.png")
photo_label = Label(main_window, image=photo)
photo_label.place(x=0,y=0)

heading = Label(main_window,
    text = "Welcome to Chess",
    font = ("Alef", 35, "bold"),
    fg = "green",
    bg="white")

heading.pack()

sign_in_button = Button(main_window,
    text = "Sign In",
    font = ("Arial",12),
    command = main_signin,
    padx=5.3)
sign_in_button.pack()

sign_up_button = Button(main_window,
    text = "Sign Up",
    font = ("Arial",12),
    command = main_signup)
sign_up_button.pack()

main_window.mainloop()
