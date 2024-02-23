import pygame
import cv2
import numpy as np
import random
from cvzone.HandTrackingModule import HandDetector
import time


# initialize
pygame.init()

# create window/display
width, height = 1138, 640
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Balloon Pop")

# Initialize clock for FPS
fps = 30
clock = pygame.time.Clock()


# webcam.
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # width
cap.set(4, 720)   # height


# Images 
imgBalloon = pygame.image.load('./Resources/BalloonRed.png').convert_alpha()
rectBalloon = imgBalloon.get_rect()
rectBalloon.x, rectBalloon.y = 500, 300

# variables
speed = 3
score = 0
startTime = time.time()
totalTime = 60


# detector
detector = HandDetector(detectionCon=0.8, maxHands=1)


# reset the ballon every it reaches the top and choose random location.
def resetBalloon():
    global speed
    rectBalloon.x = random.randint(100, img.shape[1] - 200)
    rectBalloon.y = img.shape[0] + 50
    speed += 1
 

# main loop 
start = True
while start:
    # get event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # apply logic 
    timeRemain = int(totalTime - (time.time() - startTime))
    if timeRemain < 0:
        window.fill((255, 255, 255))

        font = pygame.font.Font('./Resources/Marcellus-Regular.ttf',70)
        textScore = font.render(f'Your Score: {score}', True, (50, 50, 255))
        textTime = font.render(f'Time Up', True, (50, 50, 255))
        window.blit(textScore, (350,310))
        window.blit(textTime, (390,225))


    else:
      # opencv display
      success, img = cap.read()
    
      img = cv2.flip(img, 1)
      hands, img = detector.findHands(img, flipType=False)

      # move the balloon up
      rectBalloon.y -= speed
    
      # check if the balloon moves to the top without pop.
      if rectBalloon.y < 0:
          resetBalloon()
    
      # if hand gets detected.
      if hands:
          hand = hands[0]
          x, y = hand['lmList'][8][0:2]
          if rectBalloon.collidepoint(x, y):
              resetBalloon()
              score += 5

      imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
      imgRGB = np.rot90(imgRGB)   # rotate the image frame to 90, because the image is not straight.
      frame = pygame.surfarray.make_surface(imgRGB).convert()
      frame = pygame.transform.flip(frame, True, False)
      window.blit(frame, (0,0))

      window.blit(imgBalloon, rectBalloon)

      font = pygame.font.Font('./Resources/Marcellus-Regular.ttf',40)
      textScore = font.render(f'Score: {score}', True, (50, 50, 255))
      textTime = font.render(f'Time: {timeRemain}', True, (50, 50, 255))
      window.blit(textScore, (35,35))
      window.blit(textTime, (960,35))



    # update display
    pygame.display.update()

    # set FPS
    clock.tick(fps)

