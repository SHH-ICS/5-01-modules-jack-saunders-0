# Using the pygame library, draw a simple picture. 
# It can be anything you like, but you must use at least 2 different types of shapes and 3 different colors.
# Q4Picture.py

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
width, height = 500, 500
screen = pygame.display.set_mode((width, height))

# Set the window title
pygame.display.set_caption("Simple Picture")

# Define colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Fill the background with white color
screen.fill(WHITE)

# Draw a blue rectangle
pygame.draw.rect(screen, BLUE, (100, 100, 200, 150))

# Draw a red circle
pygame.draw.circle(screen, RED, (300, 300), 50)

# Draw a yellow line
pygame.draw.line(screen, YELLOW, (50, 450), (450, 450), 5)

# Update the display to show the drawing
pygame.display.flip()

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
sys.exit()
