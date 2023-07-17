import pygame
from numpy import random as rand
import numpy as np
import time
import json

with open("mazes.json","r") as f:
    mazes = json.load(f)

ind = len(mazes)
# Modify the data
grid_width = mazes[str(ind)]["grid_width"] 
grid_height = mazes[str(ind)]["grid_height"]
cell_size = mazes[str(ind)]["cell_size"]
border_width = mazes[str(ind)]["border_width"]
grid = mazes[str(ind)]["grid"]

# Initialize the Pygame window
window_width = grid_width * cell_size
window_height = grid_height * cell_size
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Maze")

def draw_grid():
    # Clear the window
    window.fill((255, 255, 255))  # White color in RGB

    # Draw the grid
    for row in range(grid_height):
        for col in range(grid_width):
            cell_x = col * cell_size
            cell_y = row * cell_size

            # Draw the cell color
            if grid[row][col]['color']:
                pygame.draw.rect(window, grid[row][col]['color'], (cell_x, cell_y, cell_size, cell_size))

            # Draw the top wall
            if grid[row][col]['top']:
                pygame.draw.line(window, (0, 0, 0), (cell_x, cell_y), (cell_x + cell_size, cell_y), border_width)

            # Draw the right wall
            if grid[row][col]['right']:
                pygame.draw.line(window, (0, 0, 0), (cell_x + cell_size, cell_y), (cell_x + cell_size, cell_y + cell_size), border_width)

            # Draw the bottom wall
            if grid[row][col]['bottom']:
                pygame.draw.line(window, (0, 0, 0), (cell_x + cell_size, cell_y + cell_size), (cell_x, cell_y + cell_size), border_width)

            # Draw the left wall
            if grid[row][col]['left']:
                pygame.draw.line(window, (0, 0, 0), (cell_x, cell_y + cell_size), (cell_x, cell_y), border_width)

    # Update the display
    pygame.display.update()

draw_grid()

# Keep the window open until manually closed
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
