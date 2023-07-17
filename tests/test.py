import pygame

# Set up the grid parameters
grid_width = 10  # Number of cells in the grid horizontally
grid_height = 10  # Number of cells in the grid vertically
cell_size = 50  # Size of each cell in pixels

pygame.display.set_caption("Test")

# Initialize the Pygame window
window_width = grid_width * cell_size
window_height = grid_height * cell_size
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Grid with Walls")

# Create the grid data structure
grid = [[{'top': False, 'right': True, 'bottom': False, 'left': True} for _ in range(grid_width)] for _ in range(grid_height)]

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear the window
    window.fill((255, 255, 255))  # White color in RGB

    # Draw the grid
    for row in range(grid_height):
        for col in range(grid_width):
            cell_x = col * cell_size
            cell_y = row * cell_size

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

# Quit Pygame
pygame.quit()
