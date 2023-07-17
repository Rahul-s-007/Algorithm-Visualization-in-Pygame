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
grid = [[{'top': True, 'right': True, 'bottom': True, 'left': True, 'color': None} for _ in range(grid_width)] for _ in range(grid_height)]

# Set some cells as grey and red
grid[2][3]['color'] = (128, 128, 128)  # Grey color in RGB
grid[5][7]['color'] = (255, 0, 0)  # Red color in RGB

# Helper function to get the clicked cell based on the mouse position
def get_clicked_cell(mouse_pos):
    cell_row = mouse_pos[1] // cell_size
    cell_col = mouse_pos[0] // cell_size
    return cell_row, cell_col

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button click
            mouse_pos = pygame.mouse.get_pos()
            clicked_cell = get_clicked_cell(mouse_pos)

            # Check if the clicked cell is valid
            if 0 <= clicked_cell[0] < grid_height and 0 <= clicked_cell[1] < grid_width:
                cell_row, cell_col = clicked_cell
                cell_x = cell_col * cell_size
                cell_y = cell_row * cell_size

                # Check which wall was clicked (top, right, bottom, left) and remove it
                if 0 <= mouse_pos[0] - cell_x < cell_size // 2:
                    grid[cell_row][cell_col]['left'] = False
                    if cell_col > 0:
                        grid[cell_row][cell_col - 1]['right'] = False
                elif 0 <= mouse_pos[1] - cell_y < cell_size // 2:
                    grid[cell_row][cell_col]['top'] = False
                    if cell_row > 0:
                        grid[cell_row - 1][cell_col]['bottom'] = False
                elif 0 <= mouse_pos[0] - cell_x < cell_size and cell_col < grid_width - 1:
                    grid[cell_row][cell_col]['right'] = False
                    if cell_col < grid_width - 1:
                        grid[cell_row][cell_col + 1]['left'] = False
                elif 0 <= mouse_pos[1] - cell_y < cell_size and cell_row < grid_height - 1:
                    grid[cell_row][cell_col]['bottom'] = False
                    if cell_row < grid_height - 1:
                        grid[cell_row + 1][cell_col]['top'] = False

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

# Quit Pygame
pygame.quit()
