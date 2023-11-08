import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Load an image (replace with your spaceship's image)
spaceship_image = pygame.image.load("../spaceship_sprite.png")

# Get the rect for the spaceship image
spaceship_rect = spaceship_image.get_rect()

# Calculate the initial position to center the spaceship
spaceship_x = (screen_width - spaceship_rect.width) // 2
spaceship_y = (screen_height - spaceship_rect.height) // 2

# Initial rotation angle (in degrees)
rotation_angle = 0

# Rotation speed
rotation_speed = 2  # Adjust this value to control the rotation speed

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the rotation angle at each iteration for continuous rotation
    rotation_angle += rotation_speed

    # Clear the screen
    screen.fill((0, 0, 0))

    # Rotate the spaceship's image
    rotated_spaceship = pygame.transform.rotate(spaceship_image, rotation_angle)

    # Calculate the rect for the rotated spaceship to keep it centered
    rotated_rect = rotated_spaceship.get_rect(center=spaceship_rect.center)

    # Blit the rotated spaceship onto the screen
    screen.blit(rotated_spaceship, rotated_rect.topleft)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()
