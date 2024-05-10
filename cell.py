from tkinter import Button , Label
import settings
import random
import ctypes 
import sys


class Cell :

    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None
    cell_lives_count_object = None


    def __init__(self , x , y ,is_mine = False, is_open = False, is_marked = False) :
        self.is_mine = is_mine
        self.is_open = is_open 
        self.is_marked = is_marked
        self.cell_btn_object = None
        self.x = x 
        self.y = y

        Cell.all.append(self)
    
    def create_btn_object(self , location):
        btn = Button(
            location,
            width= settings.CELL_WIDTH,
            height= settings.CELL_HEIGHT,
        )
        
        # Events :
        btn.bind('<Button-1>' , self.left_click_actions )
        btn.bind('<Button-3>' , self.right_click_actions )
        self.cell_btn_object = btn


    @staticmethod
    def create_cell_count_label(location):
        lbl = Label (
            location,
            text= f'Cells Left : {Cell.cell_count}',
            background= 'black',
            foreground= 'White',
            font = ('Agency' , 12)
        )
        Cell.cell_count_label_object = lbl

    @staticmethod
    def create_lives_count_label(location):
        lbl = Label (
            location,
            text= f'Lives : {settings.LIVES}',
            background= 'black',
            foreground= 'White',
            font = ('Agency' , 12)
        )
        Cell.cell_lives_count_object = lbl


    def get_cell_by_axis(self , x , y):
        for cell in Cell.all  :
            if cell.x == x and cell.y == y :
                return cell

    def show_mine(self) :
        Cell.cell_count -= 1
        Cell.cell_count_label_object.configure( text = f'Cells Left : {Cell.cell_count}')
        if settings.LIVES == 0:
            self.cell_btn_object.configure(background='red')
            ctypes.windll.user32.MessageBoxW(0,'You Fucking Died!' , 'Game Over!' , 0)
            sys.exit()
        else :
            Cell.cell_count -= 1
            settings.LIVES  -= 1
            self.cell_btn_object.configure(background='red')
            Cell.cell_lives_count_object.configure(text = f'Lives : {settings.LIVES}' )

    @property
    def surrounding_cells(self):
        cells = [
            self.get_cell_by_axis(self.x-1 , self.y-1),
            self.get_cell_by_axis(self.x-1 , self.y),
            self.get_cell_by_axis(self.x-1 , self.y+1),
            self.get_cell_by_axis(self.x , self.y+1),
            self.get_cell_by_axis(self.x , self.y-1),
            self.get_cell_by_axis(self.x+1, self.y-1),
            self.get_cell_by_axis(self.x+1 , self.y),
            self.get_cell_by_axis(self.x+1 , self.y+1)
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells 
    
    @property
    def count_surrounded_bombs(self):
        bombs = 0 
        for cell in self.surrounding_cells:
            if cell.is_mine :
                bombs += 1
        return bombs
    
    def show_cell(self) :
       if not self.is_open : 
            Cell.cell_count -= 1
            if self.count_surrounded_bombs == 0:
               self.cell_btn_object.configure(background='azure3')
               safe_cells = self.surrounding_cells
               for cell in safe_cells:
                   if not cell.is_open :
                    Cell.cell_count -= 1
                    cell.is_open = True
                    cell.cell_btn_object.configure(background ='azure3')
            else :
               self.cell_btn_object.configure(text = self.count_surrounded_bombs)
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                text = f'Cells Left : {Cell.cell_count}'
            )
            self.cell_btn_object.configure(background='SystemButtonFace')
            self.is_open = True

        


    # Event method needs two parameters 
    def left_click_actions(self , event):
       if self.is_mine :
           self.show_mine()
       else:
           self.show_cell()
           

            

    def right_click_actions(self , event):
        if not self.is_marked :
            self.cell_btn_object.configure(background='orange')   
            self.is_marked = True
        else : 
            self.cell_btn_object.configure(background='SystemButtonFace')
            self.is_marked = False


    @staticmethod
    def randomize_mines():
        bombs = random.sample(Cell.all , settings.NUM_OF_MINES)
        for bomb in bombs:
            bomb.is_mine  = True

    def __repr__(self):
        return f"[{self.x},{self.y}]"
    