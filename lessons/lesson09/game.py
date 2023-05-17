import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('My first game')

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
c1, c2, c3 = 0, 0, 0
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# -------- Main Program Loop -----------
i = 0
while True:
    i += 1

    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            break  # Flag that we are done so we exit this loop
    # --- Game logic should go here
    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    gameDisplay.fill((c1 + i % 255, c2 + i % 125, i%55))
    pygame.draw.polygon(gameDisplay, (128, 0, 128),[(10,10),(100,100),(100,200),(200,200)])
    # --- Go ahead and update the screen with what []we've drawn.
    pygame.display.update()
    # --- Limit to 60 frames per second
    clock.tick(60)
