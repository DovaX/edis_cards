import game_engine

def evaluate_click(grids,click):
    grid=grids[0]
    row,col=grid.evaluate_row_column_indices(click)
    print(row,col)
    return(row,col)
 

########################## Game initialization ##########################

CELL_SIZE_X=60
CELL_SIZE_Y=60
POSITION_X=15
POSITION_Y=50
MARGIN=1

import pygame
import operator





class Card:
    def __init__(self,mana_cost,attack,hp,abilities,image=None):
        self.mana_cost=mana_cost
        self.attack = attack
        self.hp = hp
        self.abilities = abilities
        self.image = image

class Game:
    def __init__(self):
        self.player_on_turn=1
        self.pieces=[]
        self.new_game=False
    
    
   
#game1=Game()    

def initialize_game():
    print("NEW GAME")
    global game1
    game1=Game()

initialize_game()    
c=game_engine.Col()  

def initialize_grids(grids):
    grids.append(game_engine.Grid(8,8,position=[POSITION_X,POSITION_Y],cell_size=[CELL_SIZE_X,CELL_SIZE_Y],colors=[c.white,c.black]))
    grid=grids[0]
    for i in range(len(grid.grid)):
        for j in range(len(grid.grid[i])):
            if((7-i)*i>9):
                grid.grid[i][j]=1
    return(grids)