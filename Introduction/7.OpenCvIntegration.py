import pygame
import cv2
import numpy as np



# initialize
pygame.init()

# create window/display
width, height = 1138, 640
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Game")

# Initialize clock for FPS
fps = 30
clock = pygame.time.Clock()


# webcam.
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # width
cap.set(4, 720)   # height

# main loop 
start = True
while start:
    # get event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # apply logic 
    # opencv display
    success, img = cap.read()
    if not success:
        break
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    imgRGB = np.rot90(imgRGB)   # rotate the image frame to 90, because the image is not straight.
    frame = pygame.surfarray.make_surface(imgRGB).convert()
    window.blit(frame, (0,0))



    # update display
    pygame.display.update()

    # set FPS
    clock.tick(fps)

