from .config import *
from tkinter import *

#Creating window
window = Tk() #creates window
window.geometry(f"{AUTH_WIDTH}x{AUTH_HEIGHT}") # window dimensions
window.title(f"{TITLE}")            # window title
window.config(background = "black") # window color


#photo = PhotoImage(file = "baruto.png")

#Label
'''label = Label(
    window,
    text = "Welcome to Chess",
    font = ("monospace",28,"bold"), # font = (name,size,style)
    fg = "green", #foreground color use hex values 
    bg = "white", #background color use hex values
    relief = RAISED, #Border style
    bd = 10   ,       # Thickness
    padx = 20 ,       #Use to pad x-coordinate
    pady = 20 ,        #Use to pad y-coordinate
    #image = photo ,     #use to create image in label
    compound= "bottom" #places image relative to text'''


#label.pack()
#label.place(<x coordinate><y coordinate>)

'''#Button
def click():
    print("Your chess game is under contstruction...")
button = Button(
    window,
    text = "Wanna play chess? ",
    command= click,
    #we can add similar features like label 
    activebackground="black",
    activeforeground="pink"
)
button.pack()'''


'''#Creating entry box
def enter():
    username = entry.get() #gets entered text from the entry
    print("Fuckoff "+username)

entry = Entry(
    window,
    font = ("monospace",25,"italic"),
    show = "*"
)
entry.pack(side=LEFT) # positioning

button = Button(
    window,
    text = "enter",
    command = enter
)
button.pack(side="right")

def delete():
    entry.delete(0,END)
delete_button = Button(
    window,
    text = "Delete",
    command=delete
)
delete_button.pack(side="right")'''

#sample project code





window.mainloop()

