import pygame
from numpy import random as rand
import numpy as np
import time

# Set up the grid parameters
grid_width = 10  # Number of cells in the grid horizontally
grid_height = 10  # Number of cells in the grid vertically
cell_size = 50  # Size of each cell in pixels

# Initialize the Pygame window
window_width = grid_width * cell_size
window_height = grid_height * cell_size
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Grid with Walls")

# Create the grid data structure
grid = [[{'top': True, 'right': True, 'bottom': True, 'left': True, 'color': None} for _ in range(grid_width)] for _ in range(grid_height)]

# grid = []
# for i in range(grid_height):
#     for j in range(grid_width):
#         grid.append({'top': True, 'right': True, 'bottom': True, 'left': True, 'color': None})


# random_start = grid[rand.randint(grid_width)][rand.randint(grid_height)]

random_start = [rand.randint(grid_width),rand.randint(grid_height)]

print(random_start)

grid[random_start[0]][random_start[1]]['color'] = (255, 0, 0)  # Red color in RGB (Starting Point)
# # Set some cells as grey and red
# grid[2][3]['color'] = (128, 128, 128)  # Grey color in RGB
# grid[5][7]['color'] = (255, 0, 0)  # Red color in RGB

# Helper function to get the clicked cell based on the mouse position
def get_clicked_cell(mouse_pos):
    cell_row = mouse_pos[1] // cell_size
    cell_col = mouse_pos[0] // cell_size
    return cell_row, cell_col
        
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
                pygame.draw.line(window, (0, 0, 0), (cell_x, cell_y), (cell_x + cell_size, cell_y), 2)

            # Draw the right wall
            if grid[row][col]['right']:
                pygame.draw.line(window, (0, 0, 0), (cell_x + cell_size, cell_y), (cell_x + cell_size, cell_y + cell_size), 2)

            # Draw the bottom wall
            if grid[row][col]['bottom']:
                pygame.draw.line(window, (0, 0, 0), (cell_x + cell_size, cell_y + cell_size), (cell_x, cell_y + cell_size), 2)

            # Draw the left wall
            if grid[row][col]['left']:
                pygame.draw.line(window, (0, 0, 0), (cell_x, cell_y + cell_size), (cell_x, cell_y), 2)

    # Update the display
    pygame.display.update()

def is_valid(x,y):
    if (0<=x and x<=grid_width-1) and (0<=y and y<=grid_height-1):
        return True


def remove_wall(x,y,direction):
    if direction=="top":
        if(is_valid(x-1,y)):
            grid[x][y]['top'] = False
            grid[x-1][y]['bottom'] = False
        else:
            return False

    if direction=="right":
        if(is_valid(x,y+1)):
            grid[x][y]["right"] = False
            grid[x][y+1]["left"] = False
        else:
            return False
        
    if direction=="bottom":
        if(is_valid(x+1,y)):
            grid[x][y]['bottom'] = False
            grid[x+1][y]['top'] = False
        else:
            return False
    
    if direction=="left":
        if(is_valid(x,y-1)):
            grid[x][y]['left'] = False
            grid[x][y-1]['right'] = False
        else:
            return False
    
    return True

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            dir_lst = ["top", "right", "bottom", "left"]
            random_square = [rand.randint(grid_width),rand.randint(grid_height)]
            print(random_square)
            direction = dir_lst[rand.randint(len(dir_lst))]
            if is_valid(random_square[0],random_square[1]):
                ans = remove_wall(random_square[0],random_square[1],direction)
    draw_grid()


# Quit Pygame
pygame.quit()
