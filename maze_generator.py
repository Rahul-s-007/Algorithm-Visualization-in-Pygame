import pygame
from numpy import random as rand
import numpy as np
import time
import json

# Set up the grid parameters
# grid_width = 20  # Number of cells in the grid horizontally
# grid_height = 20  # Number of cells in the grid vertically
# cell_size = 40  # Size of each cell in pixels
# border_width = 4

grid_width = 50
grid_height = 50 
cell_size = 10  
border_width = 2

# Initialize the Pygame window
window_width = grid_width * cell_size
window_height = grid_height * cell_size
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Grid with Walls")

# Create the grid data structure
grid = [[{'top': True, 'right': True, 'bottom': True, 'left': True, 'color': None} for _ in range(grid_width)] for _ in range(grid_height)]

visited_cells = []

# grid = []
# for i in range(grid_height):
#     for j in range(grid_width):
#         grid.append({'top': True, 'right': True, 'bottom': True, 'left': True, 'color': None})


# random_start = grid[rand.randint(grid_width)][rand.randint(grid_height)]

random_start = [rand.randint(grid_width),rand.randint(grid_height)]
random_end = [rand.randint(grid_width),rand.randint(grid_height)]
end_cell = random_end

print(random_start)
print(end_cell)

visited_cells.append(random_start)

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

def is_valid(x,y):
    if (0<=x and x<=grid_width-1) and (0<=y and y<=grid_height-1):
        return True

def is_visited(x,y):
    if [x,y] in visited_cells:
        return True
    return False

def get_neighbour(x,y):
    available_direction = []
    if(is_valid(x-1,y) and is_visited(x-1,y) == False):
        available_direction.append("top")
    if(is_valid(x,y+1) and is_visited(x,y+1) == False):
        available_direction.append("right")
    if(is_valid(x+1,y) and is_visited(x+1,y) == False):
        available_direction.append("bottom")
    if(is_valid(x,y-1) and is_visited(x,y-1) == False):
        available_direction.append("left")

    return available_direction

def remove_wall(x,y,direction):
    next_cell = []
    if direction=="top":
        if(is_valid(x-1,y)):
            grid[x][y]['top'] = False
            grid[x-1][y]['bottom'] = False
            next_cell = [x-1,y]
        else:
            return False

    if direction=="right":
        if(is_valid(x,y+1)):
            grid[x][y]["right"] = False
            grid[x][y+1]["left"] = False
            next_cell = [x,y+1]
        else:
            return False
        
    if direction=="bottom":
        if(is_valid(x+1,y)):
            grid[x][y]['bottom'] = False
            grid[x+1][y]['top'] = False
            next_cell = [x+1,y]
        else:
            return False
    
    if direction=="left":
        if(is_valid(x,y-1)):
            grid[x][y]['left'] = False
            grid[x][y-1]['right'] = False
            next_cell = [x,y-1]
        else:
            return False
    
    return next_cell # or True

current_cell = random_start

while(len(visited_cells)<grid_width*grid_height): #to check when maze over
    available_direction = get_neighbour(current_cell[0],current_cell[1])
    if len(available_direction) == 0:
        back_track = -1
        available_direction = get_neighbour(visited_cells[back_track][0],visited_cells[back_track][1])
        current_cell = [visited_cells[back_track][0],visited_cells[back_track][1]]
        while(len(available_direction) == 0):
            back_track = back_track-1
            available_direction = get_neighbour(visited_cells[back_track][0],visited_cells[back_track][1])
            current_cell = [visited_cells[back_track][0],visited_cells[back_track][1]]
    
    random_direction = available_direction[rand.randint(len(available_direction))]
    new_current_cell = remove_wall(current_cell[0],current_cell[1],random_direction)
    if new_current_cell == False:
        print("Error")
        break
    current_cell = new_current_cell
    grid[current_cell[0]][current_cell[1]]['color'] = (128, 128, 128)  # Grey color in RGB
    visited_cells.append([current_cell[0],current_cell[1]])

    if current_cell == end_cell:
        grid[current_cell[0]][current_cell[1]]['color'] = (0, 255, 0)  # Green color in RGB
    
    draw_grid()

def save_maze():
    with open("mazes.json","r") as f:
        mazes = json.load(f)

    ind = len(mazes)
    # Modify the data
    mazes[str(ind+1)] = {"grid_width":grid_width, 
                        "grid_height":grid_height, 
                        "cell_size": cell_size, 
                        "border_width":border_width,
                        "grid":grid}

    # Write the modified data back to the file
    with open('mazes.json', 'w') as file:
        json.dump(mazes, file, indent=4)

save_maze()

# Keep the window open until manually closed
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
