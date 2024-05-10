from tkinter import *
from cell import Cell
import settings
import utility

# root is our window
root = Tk() # Start
# OverWriting the Setting of "root"

root.configure( background = 'black' )
root.title("Sep's Mine Sweeper")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.resizable(False,False) # one for the widlth , one for the height

# Making the frame :
top_frame = Frame(
    root,
    background = 'black',
    width = settings.WIDTH,
    height = utility.height_prct(18)
)
# Placing the frame : 
top_frame.place(x=0 , y=0)

left_frame = Frame(
    root,
    background = 'black',
    width = utility.width_prct(18),
    height = settings.HEIGHT
)
left_frame.place(x=0 , y=0)

center_frame = Frame(
    root,
    background='black',
    width = utility.width_prct(82),
    height = utility.height_prct(82)
)
center_frame.place(x = utility.width_prct(20) , y = utility.height_prct(20) )


utility.place_field(center_frame)
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x = 0 , y = 0)
Cell.create_lives_count_label(left_frame)
Cell.cell_lives_count_object.place(x = 0 , y = 22)
Cell.randomize_mines()   


root.mainloop() # Finish