import pygame
import numpy as np #For multidimensional arrays, used as grid and rows
import time
import random #Will be used later to set the cell to alive or dead


#Creating an object called game
class Game:
    def __init__(self, width, height, area, offset):
        self.area = area #Area of each square, the bigger the area the bigger the square
        #Numbers of row and cols is relative to the width and height and the area
        self.col = int(width/area) #Number of columns relative to width
        self.row = int(height/area) #Number of rows relative to the height
        self.size = (self.row, self.col) # Tuple
        self.grid_array = np.ndarray(shape=(self.size)) #Shape is a parameter in the ndarray() function that shapes !! Must be a tuple !!
        self.offset = offset #Border width

    #This function is used to define new cells from 0
    def init_cells(self):
        #Looping in each cell
        for x in range(self.row):
            for y in range(self.col):
                self.grid_array[x][y] = random.randint(0,1) # Return an integer, 0 or 1

    #This function will define each cell's color depending on it status
    #This function will also set the 
    def this_cell(self, aliveCol, deadCol, bg_Color):
        for x in range(self.row):
            for y in range(self.col):
                #Get the coordinance of the current cell
                y_pos = y * self.area 
                x_pos = x * self.area
                #If the cell is alive == 1 we give it the alive color 
                if self.grid_array[x][y] == 1:
                    pygame.draw.rect(bg_Color, aliveCol, [x_pos, y_pos, self.area-self.offset, self.area-self.offset])
                #If the cell is dead == 0 we will give it the dead color 
                else:
                    pygame.draw.rect(bg_Color, deadCol, [x_pos, y_pos, self.area-self.offset, self.area-self.offset])

        next = np.ndarray(shape=(self.size))
        for x in range(self.row):
            for y in range(self.col):
                state = self.grid_array[x][y]
                neighbours = self.get_neighbours( x, y)
                if state == 0 and neighbours == 3:
                    next[x][y] = 1
                elif state == 1 and (neighbours < 2 or neighbours > 3):
                    next[x][y] = 0
                else:
                    next[x][y] = state
        self.grid_array = next

    def get_neighbours(self, x, y):
        totalNeighbours = 0 
        for n in range(-1, 2):
            for m in range(-1, 2):
                x_edge = (x+n+self.row) % self.row
                y_edge = (y+m+self.col) % self.col
                totalNeighbours += self.grid_array[x_edge][y_edge]

        totalNeighbours -= self.grid_array[x][y]
        return totalNeighbours

#This is the main
size = (900, 900)
pygame.init()
mainPanel = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 1

black = (0, 0, 0)
white = (255, 255, 255)
red = (255,0,0)

#Initialize the Game object with given params
newGame = Game(900,900, 20, 1)
newGame.init_cells()

status = True
while status:
    clock.tick(fps)
    mainPanel.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False

    newGame.this_cell(deadCol=white, aliveCol=red, bg_Color=mainPanel)
    pygame.display.update()

pygame.quit()