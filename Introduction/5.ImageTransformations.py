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
# convert() is used to have smooth transitioning.
imgBackground = pygame.image.load('./Resources/BackgroundBlue.jpg').convert()
# convert_alpha() is used because the image is in png format.
imgBalloonRed = pygame.image.load('./Resources/BalloonRed.png').convert_alpha()

# transforming an image.
# 1. rotating an image through a certain angle.
# imgBalloonRed = pygame.transform.rotate(imgBalloonRed, 90)
# rotating and scaling the image
# imgBalloonRed = pygame.transform.rotozoom(imgBalloonRed, 90, 5)
# 2. flip an image.
# flip to x and y axis.
# imgBalloonRed = pygame.transform.flip(imgBalloonRed, False, True)


# main loop 
start = True
while start:
    # get event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # apply logic 
            
    # 3. scaling of an image.
    # imgBalloonRed = pygame.transform.scale(imgBalloonRed, (150, 150))
    # for the smoothness of the edges of the image.
    # imgBalloonRed = pygame.transform.smoothscale(imgBalloonRed, (150, 150))
            
            
    window.blit(imgBackground, (0,0))
    window.blit(imgBalloonRed, (100,100))

    # update display
    pygame.display.update()

    # set FPS
    clock.tick(fps)

