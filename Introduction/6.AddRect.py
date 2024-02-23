# in order to change the location of object in an image, we draw a rectangle of same size as that of object, as we ...
# ... change the location of the rectangle, the position of the object will get changed ultimately.
import pygame

# initialize
pygame.init()

# create window/display
width, height = 1138, 640
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Game")

# Initialize clock for FPS
fps = 30
clock = pygame.time.Clock()


# load Images
imgBackground = pygame.image.load('./Resources/BackgroundBlue.jpg').convert()
# convert_alpha() is used because the image is in png format.
imgBalloonRed = pygame.image.load('./Resources/BalloonRed.png').convert_alpha()

# get the rectangle of same size as that of balloon.
# two ways of creating a rect.
# 1. pygame.Rect(x, y, width, height)
# 2. surface.get_rect()
rectBalloon = imgBalloonRed.get_rect()

# Rect
rectBalloon1 = pygame.Rect(500, 0, 200, 200) 

# main loop 
start = True
while start:
    # get event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # apply logic
    # to check the collision between two rects. (first rect hits the second)
    print(rectBalloon.colliderect(rectBalloon1))    # collide = true else false.
    # access the x and y coordinates in order to move the rectangle. 
    rectBalloon.x += 2
    # rectBalloon.y += 5

    window.blit(imgBackground, (0,0))

    # pygame.draw.rect(window, (0, 255, 0), rectBalloon)
    # pygame.draw.rect(window, (0, 255, 0), rectBalloon1)
    window.blit(imgBalloonRed, rectBalloon)

    # update display
    pygame.display.update()

    # set FPS
    clock.tick(fps)

