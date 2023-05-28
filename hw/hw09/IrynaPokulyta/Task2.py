# You need to change the code in the Rect_pygame.py program
# so that the rectange does not extend beyond the program window

import pygame
pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('My first game')

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Loop until the user clicks the close button.
done = True
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# -------- Main Program Loop -----------
i = 0
while done:
    i += 1

    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = False  # Flag that we are done so we exit this loop
    # --- Game logic should go here
    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    gameDisplay.fill(RED)
    pygame.draw.rect(gameDisplay, BLACK, [50, 50, 100, 200])
    # --- Go ahead and update the screen with what []we've drawn.
    pygame.display.update()
    # --- Limit to 60 frames per second
    clock.tick(60)
