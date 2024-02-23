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

# main loop 
start = True
while start:
    # get event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # apply logic 
    window.blit(imgBackground, (0,0))
    window.blit(imgBalloonRed, (100,100))

    # update display
    pygame.display.update()

    # set FPS
    clock.tick(fps)

