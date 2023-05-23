# import pygame
# pygame.init()
# gameDisplay=pygame.display.set_mode((800,600))
# pygame.display.set_caption('My first game')
# clock=pygame.time.Clock()
# WHITE=(255,255,255)
# c1, c2, c3 = 0, 0, 0
# done=False
# i=0
# while not done:
#     i+=1
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             done=True
#             print("User asked to quit")
#         # elif event.type==pygame.KEYDOWN:
#         #     print("User pressed a key Down")
#         # elif event.type == pygame.KEYUP:
#         #     print("User pressed a key UP")
#     gameDisplay.fill((c1 + i % 255, c2 + i % 125, i % 55))
#     pygame.draw.polygon(gameDisplay, (128, 0, 128), [(10, 10), (100, 100), (100, 200), (200, 200)])
# #    gameDisplay.fill(WHITE)
#     pygame.display.update()
#     clock.tick(60)


import pygame

FPS = 60

WIDTH_DISPLAY = 500
HEIGHT_DISPLAY = 500

COORD_X = 50
COORD_Y = 50
WIDTH_RECTANGLE = 40
HEIGHT_RECTANGLE = 60
DELTA_STEP = 5

BLACK_COLOR = (0, 0, 0)
RED_COLOR = (250, 0, 0)

pygame.init()

gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY), pygame.RESIZABLE)

pygame.display.set_caption("My first game")

run = True
clock = pygame.time.Clock()

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        COORD_X = COORD_X - DELTA_STEP
        if COORD_X==0:
            COORD_X = DELTA_STEP
    if keys[pygame.K_RIGHT]:
        COORD_X = COORD_X + DELTA_STEP
        if COORD_X>=WIDTH_DISPLAY-WIDTH_RECTANGLE:
            COORD_X = WIDTH_DISPLAY-WIDTH_RECTANGLE
    if keys[pygame.K_UP]:
        COORD_Y = COORD_Y - DELTA_STEP
        if COORD_Y == 0:
            COORD_Y=DELTA_STEP
    if keys[pygame.K_DOWN]:
        COORD_Y = COORD_Y + DELTA_STEP
        if COORD_Y >= HEIGHT_DISPLAY-HEIGHT_RECTANGLE:
            COORD_Y=HEIGHT_DISPLAY-HEIGHT_RECTANGLE

    gameDisplay.fill(BLACK_COLOR)

    pygame.draw.rect(gameDisplay, RED_COLOR, [COORD_X,
                                              COORD_Y,
                                              WIDTH_RECTANGLE,
                                              HEIGHT_RECTANGLE])
    pygame.display.update()
    clock.tick(FPS)






