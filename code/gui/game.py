from tkinter import *
from ..classes.vars import position_color_relation
from .config import *

game_window = Tk()
game_window.geometry(f"{GAME_WIDTH}x{GAME_HEIGHT}")
game_window.grid_columnconfigure(0, weight=1)

'''heading = Label(game_window,
                fg = "White",
                bg = "Black")
heading.grid(row=0, column=0)'''



for row in range(8, 0, -1):
    new_row_frame = Frame(game_window, width=GAME_WIDTH, height=GAME_HEIGHT // 8)
    new_row_frame.grid(row = 8 - row + 1, column = 0, pady=20)
    new_row_frame.grid_propagate(False)
    for column in range(97, 105):
        position_name = f'{chr(column)}{row}'
        new_tile = Button(new_row_frame, bg = position_color_relation[position_name], width = GAME_WIDTH // 8, height = GAME_HEIGHT // 8)
        new_row_frame.grid_columnconfigure(column - 97, weight=0)
        new_tile.grid(row=0,column=column-97)

#Button(game_window, text="Button-1",height= 5, width=10).pack()

'''_
chess engine


tile - tile - tile - tile --- tile
|       
|
|
tile - tile - tile - tile --- tile

'''

game_window.mainloop()