# Using the pygame library, draw a simple picture. 
# It can be anything you like, but you must use at least 2 different types of shapes and 3 different colors.
# Q4Picture.py

import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the display window
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Q4 Picture")

# Define colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Fill the screen with white color
screen.fill(WHITE)

# Draw shapes
pygame.draw.rect(screen, RED, pygame.Rect(50, 50, 200, 100))  # Red rectangle
pygame.draw.circle(screen, GREEN, (300, 300), 50)  # Green circle
pygame.draw.line(screen, BLUE, (50, 50), (350, 350), 5)  # Blue line

# Update the display
pygame.display.flip()

# Keep the window open
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

