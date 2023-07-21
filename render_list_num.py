import pygame
import sys
import random

# Initialize Pygame
pygame.init()

DELAY = 5  # Milliseconds between screen updates

# Set up the screen
screen_width = 1000
screen_height = 550
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Vertical Poles Rendering")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255,0,0)
GREEN = (0,255,0)
#------------------------------------------------------------
"""
pole_width is the width of each pole, which is set to 20 pixels in this case.
spacing is the space between each pole, which is set to 0 pixels, so the poles will be drawn directly beside each other.
x_position is the starting x-position for the first pole, initially set to 0.
Inside the loop, the function iterates over each height in the heights_list. It calculates the pole_height based on the current height value from the list.
Then, it creates a pygame.Rect object called pole_rect that represents the rectangular shape of the pole. The x and y coordinates of the rectangle are determined by the current x_position and the screen height minus the pole_height to place the pole from the bottom of the screen.
It draws the pole using pygame.draw.rect() with WHITE color and pole_rect.
Additionally, a black border is drawn around the pole using pygame.draw.rect() with BLACK color and pole_rect as the rectangle object. The 2 parameter specifies the width of the border (2 pixels in this case).
Finally, the x_position is updated to move to the next position for the next pole.
"""
# Function to render the poles
def render_poles(heights_list, index1, index2):
    screen.fill(BLACK)  # Fill the screen with black color
    pole_width = 20  # Width of each pole
    spacing = 0     # Space between each pole

    x_position = 0  # Starting x-position for the first pole

    for i,height in enumerate(heights_list):
        pole_height = height
        pole_rect = pygame.Rect(x_position, screen_height - pole_height, pole_width, pole_height)

        # Draw the pole
        if i == index1 or i == index2:
            pygame.draw.rect(screen, RED, pole_rect)
        elif index1 == -1 and index2 == -1:
            pygame.draw.rect(screen, GREEN, pole_rect)
        else:
            pygame.draw.rect(screen, WHITE, pole_rect)

        # Draw the black border around the pole
        pygame.draw.rect(screen, BLACK, pole_rect, 2)

        # Move the x-position for the next pole
        x_position += pole_width + spacing
    pygame.display.update()
    # pygame.time.delay(100) # Delay for 100 milliseconds
    pygame.time.delay(DELAY) # Delay for 100 milliseconds

#------------------------------------------------------------
"""
start, stop, and step are parameters used to define the range of numbers for the list.
size is the desired size of the generated random list.
The function first generates a numbers_list using the range() function with the given start, stop, and step parameters.
Then, if the desired size is larger than the number of elements in the numbers_list, it calculates the number of repetitions needed to have enough elements for random sampling and repeats the list accordingly.
Finally, it uses random.sample() to randomly sample size elements from the numbers_list without replacement and returns the resulting random_list.
"""
# This function generates a list of continuous numbers or numbers with a constant step in random order.
def generate_random_list(start, stop, step, size):
    # Generate the list of continuous numbers or numbers with a constant step
    numbers_list = list(range(start, stop, step))

    # If the desired size is larger than the number of elements in the list,
    # repeat the list to have enough elements for random sampling.
    if size > len(numbers_list):
        repetitions = size // len(numbers_list) + 1
        numbers_list = numbers_list * repetitions

    # Randomly sample 'size' elements from the list
    random_list = random.sample(numbers_list, size)

    return random_list

#------------------------------------------------------------
start_number = 10
end_number = 510
step_size = 10
list_size = 50

random_numbers = generate_random_list(start_number, end_number, step_size, list_size)
print(random_numbers)
print(len(random_numbers))

# List of heights (you can use your own list here)
lst = random_numbers

sorting_over = False
green_render = False
# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if sorting_over == False:
        print("new start")
        # Your sorting algorithm goes here
        swapped = False # used to exit when list is sorted
        # Traverse through all array elements
        swapped = True
        render_poles(lst, "current_index/s") 
        print(swapped)
        if swapped == False:
            sorting_over = True
            break

    else:
        if not green_render:
            render_poles(lst, -1, -1) # -1 means no index is red colour and all in green
            pygame.time.delay(1000) # Delay for 100 milliseconds so green visible
            green_render = True

        render_poles(lst, -2, -1) # -2 means all index is white colour

"""
# Version-2
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 1000
screen_height = 550
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Vertical Poles Rendering")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#------------------------------------------------------------
"""
# pole_width is the width of each pole, which is set to 20 pixels in this case.
# spacing is the space between each pole, which is set to 0 pixels, so the poles will be drawn directly beside each other.
# x_position is the starting x-position for the first pole, initially set to 0.
# Inside the loop, the function iterates over each height in the heights_list. It calculates the pole_height based on the current height value from the list.
# Then, it creates a pygame.Rect object called pole_rect that represents the rectangular shape of the pole. The x and y coordinates of the rectangle are determined by the current x_position and the screen height minus the pole_height to place the pole from the bottom of the screen.
# It draws the pole using pygame.draw.rect() with WHITE color and pole_rect.
# Additionally, a black border is drawn around the pole using pygame.draw.rect() with BLACK color and pole_rect as the rectangle object. The 2 parameter specifies the width of the border (2 pixels in this case).
# Finally, the x_position is updated to move to the next position for the next pole.
"""
# Function to render the poles
def render_poles(heights_list):
    pole_width = 20  # Width of each pole
    spacing = 0     # Space between each pole

    x_position = 0  # Starting x-position for the first pole

    for height in heights_list:
        pole_height = height
        pole_rect = pygame.Rect(x_position, screen_height - pole_height, pole_width, pole_height)

        # Draw the pole
        pygame.draw.rect(screen, WHITE, pole_rect)

        # Draw the black border around the pole
        pygame.draw.rect(screen, BLACK, pole_rect, 2)

        # Move the x-position for the next pole
        x_position += pole_width + spacing


#------------------------------------------------------------
"""
# start, stop, and step are parameters used to define the range of numbers for the list.
# size is the desired size of the generated random list.
# The function first generates a numbers_list using the range() function with the given start, stop, and step parameters.
# Then, if the desired size is larger than the number of elements in the numbers_list, it calculates the number of repetitions needed to have enough elements for random sampling and repeats the list accordingly.
# Finally, it uses random.sample() to randomly sample size elements from the numbers_list without replacement and returns the resulting random_list.
"""
# This function generates a list of continuous numbers or numbers with a constant step in random order.
def generate_random_list(start, stop, step, size):
    # Generate the list of continuous numbers or numbers with a constant step
    numbers_list = list(range(start, stop, step))

    # If the desired size is larger than the number of elements in the list,
    # repeat the list to have enough elements for random sampling.
    if size > len(numbers_list):
        repetitions = size // len(numbers_list) + 1
        numbers_list = numbers_list * repetitions

    # Randomly sample 'size' elements from the list
    random_list = random.sample(numbers_list, size)

    return random_list

#------------------------------------------------------------
start_number = 10
end_number = 510
step_size = 10
list_size = 50

random_numbers = generate_random_list(start_number, end_number, step_size, list_size)
print(random_numbers)
print(len(random_numbers))

# List of heights (you can use your own list here)
heights_list = random_numbers

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)  # Fill the screen with black color

    render_poles(heights_list)

    pygame.display.flip()  # Update the display
"""

"""
# Version-1
import pygame
import sys

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)  # White
POLE_COLOR = (0, 0, 0)  # Black
POLE_WIDTH = 20
POLE_SPACING = 30
MAX_POLE_HEIGHT = HEIGHT - 50  # Limit the height of the poles to prevent them from going off the screen

def render_poles(heights, screen):
    x = POLE_SPACING
    for height in heights:
        pole_height = min(height, MAX_POLE_HEIGHT)
        pygame.draw.rect(screen, POLE_COLOR, (x, HEIGHT - pole_height, POLE_WIDTH, pole_height))
        x += POLE_WIDTH + POLE_SPACING

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Vertical Poles Renderer")

    # Sample list of heights (modify this list with your data)
    pole_heights = [150, 200, 100, 300, 250, 180]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BACKGROUND_COLOR)
        render_poles(pole_heights, screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
"""