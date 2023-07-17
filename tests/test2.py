import pygame

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
grid = [[{'top': True, 'right': True, 'bottom': True, 'left': True} for _ in range(grid_width)] for _ in range(grid_height)]

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button click
            mouse_pos = pygame.mouse.get_pos()
            clicked_cell = (mouse_pos[1] // cell_size, mouse_pos[0] // cell_size)  # Calculate the clicked cell

            # Check if the clicked cell is valid
            if 0 <= clicked_cell[0] < grid_height and 0 <= clicked_cell[1] < grid_width:
                # Remove walls between the clicked cell and its neighboring cell on the right
                if clicked_cell[1] < grid_width - 1:
                    grid[clicked_cell[0]][clicked_cell[1]]['right'] = False
                    grid[clicked_cell[0]][clicked_cell[1] + 1]['left'] = False

                # Remove walls between the clicked cell and its neighboring cell on the bottom
                if clicked_cell[0] < grid_height - 1:
                    grid[clicked_cell[0]][clicked_cell[1]]['bottom'] = False
                    grid[clicked_cell[0] + 1][clicked_cell[1]]['top'] = False

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
