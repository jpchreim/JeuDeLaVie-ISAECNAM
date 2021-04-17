import pygame
import time
import random
import numpy as np
import os
#Creating an object called game
class Game:
    def __init__(self, width, height, scale, offset):
        self.scale = scale
        #Numbers of row and cols is relative to the width and height and the scale
        self.col = int(height/scale)
        self.row = int(width/scale)
        self.size = (self.row, self.col)
        self.grid_array = np.ndarray(shape=(self.size))
        self.offset = offset
    #This function is used to define new cells from 0
    def init_cells(self):
        #Looping in each cell
        for x in range(self.row):
            for y in range(self.col):
                #will set each cell to 0 or 1
                self.grid_array[x][y] = random.randint(0,1)

    #This function will define each cell's color depending on it status
    #This function will also set the 
    def this_cell(self, aliveCol, deadCol, bg_Color):
        for x in range(self.row):
            for y in range(self.col):
                y_pos = y * self.scale
                x_pos = x * self.scale
                #random_color = (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255))
                if self.grid_array[x][y] == 1:
                    pygame.draw.rect(surface, on_color, [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])
                else:
                    pygame.draw.rect(surface, off_color, [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])

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
        total = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                x_edge = (x+n+self.row) % self.row
                y_edge = (y+m+self.col) % self.col
                total += self.grid_array[x_edge][y_edge]

        total -= self.grid_array[x][y]
        return total