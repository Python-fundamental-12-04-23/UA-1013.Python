import pygame

FPS = 60

WIDTH_DISPLAY = 500
HEIGHT_DISPLAY = 500

COORD_X = 50
COORD_Y = 50
WIDTH_RECTANGLE = 40
HEIGHT_RECTANGLE = 60
DELAY = 10
DELTA_STEP = 3

BLACK_COLOR = (0, 0, 0)
RED_COLOR = (250, 0, 0)

pygame.init()

gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY), pygame.RESIZABLE)

pygame.display.set_caption("My first game")

run = True
clock = pygame.time.Clock()

while run:
    pygame.time.delay(DELAY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        COORD_X = COORD_X - DELTA_STEP
    elif keys[pygame.K_RIGHT]:
        COORD_X = COORD_X + DELTA_STEP
    if keys[pygame.K_UP]:
        COORD_Y = COORD_Y - DELTA_STEP
    elif keys[pygame.K_DOWN]:
        COORD_Y = COORD_Y + DELTA_STEP
    COORD_X = min(WIDTH_DISPLAY - WIDTH_RECTANGLE, max(0, COORD_X))
    COORD_Y = min(HEIGHT_DISPLAY - HEIGHT_RECTANGLE, max(0, COORD_Y))

    gameDisplay.fill(BLACK_COLOR)

    pygame.draw.rect(gameDisplay, RED_COLOR, [COORD_X,
                                              COORD_Y,
                                              WIDTH_RECTANGLE,
                                              HEIGHT_RECTANGLE])
    pygame.display.update()
    clock.tick(FPS)
