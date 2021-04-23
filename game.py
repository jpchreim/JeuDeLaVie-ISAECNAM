import pygame
import numpy as np  # For multidimensional arrays, used as grid and rows
import time
import random  # Will be used later to set the cell to alive or dead

# Creating an object called game


class Game:
    def __init__(self, width, height, area, offset):
        self.area = area  # Area of each square, the bigger the area the bigger the square
        # Numbers of row and cols is relative to the width and height and the area
        self.col = int(width/area)  # Number of columns relative to width
        self.row = int(height/area)  # Number of rows relative to the height
        self.size = (self.row, self.col)  # Tuple
        # Shape is a parameter in the ndarray() function that shapes !! Must be a tuple !!
        self.grid_array = np.ndarray(shape=(self.size))
        self.offset = offset  # Border width

    # This function is used to define new cells from 0
    def init_cells(self):
        # Looping in each cell
        for x in range(self.row):
            for y in range(self.col):
                self.grid_array[x][y] = random.randint(
                    0, 1)  # Return an integer, 0 or 1

    # This function will be used to get the total number of cousins arround each cell
    def get_cousins(self, x, y):
        total_cousins = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                # Calculationg from the current position, x and y the position of their cousins
                calculate_surrounding = lambda n,m,l : (n+m+l)%l 
                surroundings_X = calculate_surrounding(x,n,self.row)
                surroundings_Y = calculate_surrounding(y,m,self.col)
                total_cousins += self.grid_array[surroundings_X][surroundings_Y]
        # We romved he current x and y
        total_cousins -= self.grid_array[x][y]
        return total_cousins

    # This function will define each cell's color depending on it status
    # This function will also set the
    def this_cell(self, aliveCol, deadCol, bg_Color):
        for x in range(self.row):
            for y in range(self.col):
                # Get the coordinance of the current cell
                calculate_position= lambda n,m : n * m
                position_Y = calculate_position(y,  self.area)
                position_X = calculate_position(x,  self.area)
                # If the cell is alive == 1 we give it the alive color
                if self.grid_array[x][y] == 1:
                    pygame.draw.rect(bg_Color, aliveCol, [position_X, position_Y, self.area-self.offset, self.area-self.offset])
                # If the cell is dead == 0 we will give it the dead color
                else:
                    pygame.draw.rect(bg_Color, deadCol, [position_X, position_Y, self.area-self.offset, self.area-self.offset])

        # Initialize a new 2 dimensional array that will contain the next move
        next = np.ndarray(shape=(self.size))  # The dimension won't change
        # Looping in each cell
        for x in range(self.row):
            for y in range(self.col):
                # Get the state of the current cell AND the state of the cousins
                # Will return the total number of cousins for the cell at x ,y and will store it in cousins
                cousins = self.get_cousins(x, y)
                state = self.grid_array[x][y]

                # Rules
                if state == 0 and cousins == 3:
                    next[x][y] = 1
                elif state == 1 and (cousins < 2 or cousins > 3):
                    next[x][y] = 0
                else:
                    next[x][y] = state
        self.grid_array = next  # Update the new changes

#The end of this class