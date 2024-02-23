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

# main loop 
start = True
while start:
    # get event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # apply logic 
    window.fill((255, 255, 255))
    # None - the default font, 100 is the size of the font. Can use the external file to change the font.
    font = pygame.font.Font('./Resources/Marcellus-Regular.ttf',100)
    font1 = pygame.font.Font(None,100)
    # True is antialias, to make the text look smooth.
    text = font.render("My Game", True, (50,50,50))
    text1 = font1.render("My Game", True, (50,50,50))
    window.blit(text, (390,300))
    window.blit(text1, (390,500))


    # update display
    pygame.display.update()

    # set FPS
    clock.tick(fps)

