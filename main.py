import pygame
import numpy as np  # For multidimensional arrays, used as grid and rows
import time
import random  # Will be used later to set the cell to alive or dead
from game import Game

if __name__ == "__main__":
    # This is the main
    size = (900, 900)
    pygame.init()
    # Creating the gaming panel
    mainPanel = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    # Definining the colors
    white = (255, 255, 255)
    red = (255, 0, 0)
    # The speed of the next, the lower the slower
    speed = 1

    # Initialize the Game object with given params
    newGame = Game(900, 900, 20, 1)
    newGame.init_cells()
    status = True
    while status:
        clock.tick(speed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status = False

        newGame.this_cell(red, white, mainPanel)
        pygame.display.update()

    pygame.quit()
#The end