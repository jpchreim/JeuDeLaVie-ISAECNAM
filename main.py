import pygame
import time
import random
import numpy as np
import os
import grid

#Size of the panel
width, height = 900,900
size = (width, height)

pygame.init()
#Title of the game
pygame.display.set_caption("Jeu de la vie")
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
speed = 1 #Speed of the next


black = (0, 0, 0)
blue1 = (0, 121, 150)
white = (255, 255, 255)

scaler = 40
offset = 1

Grid = grid.Grid(width,height, scaler, offset)
Grid.random2d_array()


run = True
while run:
    clock.tick(speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    Grid.Conway(off_color=white, on_color=blue1, surface=screen)
    pygame.display.update()

pygame.quit()