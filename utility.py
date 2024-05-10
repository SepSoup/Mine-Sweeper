import settings
from cell import Cell

def height_prct(percentage):
    return (settings.HEIGHT / 100) * percentage

def width_prct(percentage):
    return (settings.WIDTH / 100) * percentage

def place_field(frame):
    for i in range (settings.GRID_SIZE):
        for j in range (settings.GRID_SIZE):
            c = Cell(i,j)
            c.create_btn_object(frame)
            c.cell_btn_object.grid(column=i , row= j)
    