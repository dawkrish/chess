from tkinter import *
from ..classes.vars import position_color_relation
from .config import *

game_window = Tk()
game_window.geometry(f"{GAME_WIDTH}x{GAME_HEIGHT}")
game_window.resizable(width=False, height=False)
game_window.grid_columnconfigure(0, weight=1)

'''
heading = Label(game_window,
                fg = "White",
                bg = "Black")
heading.grid(row=0, column=0)
'''
for row in range(8, 0, -1):
    row_frame = Frame(game_window, width=GAME_WIDTH, height=GAME_HEIGHT//8)
    row_frame.grid_propagate(False)
    for column in range(97, 105):
        position = f"{chr(column)}{row}"
        btn_frame = Frame(row_frame, width=GAME_WIDTH//8,height= GAME_HEIGHT//8)
        btn_frame.grid(row=0, column=column-97)
        btn = Button(btn_frame, width=5, height=5, bg=position_color_relation[position],text=position)
        btn.grid(row=0, column=0)
    row_frame.grid(row=abs(9 - row), column=0)

'''_
chess engine


tile - tile - tile - tile --- tile
|       
|
|
tile - tile - tile - tile --- tile

'''

game_window.mainloop()