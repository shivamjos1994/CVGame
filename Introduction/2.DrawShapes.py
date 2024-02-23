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

    # apply logic.
    # color of the window screen
    window.fill((255, 255, 255))
    red, green, blue = (255, 0, 0), (0, 255, 0), (0, 0, 255)
    # polygon - surface, color, 6 coordinates of the polygon
    pygame.draw.polygon(window, red, ((380,80), (710,80), (867, 350), (788,600), (491,600), (300,350)))
    # circle - surface, color, center coordinates, radius
    pygame.draw.circle(window, green, (569,320), 150)
    # line - suface, color, starting and end coordinates
    pygame.draw.line(window, blue, (460,392), (805,392), 10)
    # rectangle - surface, color, x,y coordinates and width, height
    pygame.draw.rect(window, blue, (460, 307, 345, 70), border_radius=10)

    # pygame.draw.ellipse(window, blue, (500, 200, 100, 50), 5)
    # pygame.draw.arc(window, blue, (500, 200, 100, 50), 20.23, 140.34, 5)
    # pygame.draw.aaline(window, blue, (500, 200), (700, 200), 10)

    # update display
    pygame.display.update()

    # set FPS
    clock.tick(fps)

