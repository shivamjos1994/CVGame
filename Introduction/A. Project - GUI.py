import pygame

# initialize
pygame.init()

# create window/display
width, height = 1138, 640
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("GUI")

# Initialize clock for FPS
fps = 30
clock = pygame.time.Clock()

# Colors 
c = { 'lightGreen' : (189, 209, 197),
      'lightOrange' : (238, 204, 140),
      'lightPink' : (232, 178, 152),
      'darkPink' : (211, 162, 157),
      'darkGreen' : (158, 171, 162),
      'darkGray' : (128, 126, 126),
      'lightGray' : (204, 204, 204),
      'darkBrown' : (89, 61, 61),
      'white' : (255, 255, 255),
      'black' : (0, 0, 0)
}

# Images
imgBackground = pygame.image.load('./Resources/Project - GUI/background.png').convert()
imgDesign = pygame.image.load('./Resources/Project - GUI/design.png').convert_alpha()
imgIcon1 = pygame.image.load('./Resources/Project - GUI/icon1.png').convert_alpha()
imgIcon2 = pygame.image.load('./Resources/Project - GUI/icon2.png').convert_alpha()
imgIcon3 = pygame.image.load('./Resources/Project - GUI/icon3.png').convert_alpha()
imgIcon4 = pygame.image.load('./Resources/Project - GUI/icon4.png').convert_alpha()
imgIcon5 = pygame.image.load('./Resources/Project - GUI/icon5.png').convert_alpha()
imgShadow = pygame.image.load('./Resources/Project - GUI/shadow.png').convert_alpha()
imgToggleOn = pygame.image.load('./Resources/Project - GUI/toggleOn.png').convert_alpha()
imgToggleOff = pygame.image.load('./Resources/Project - GUI/toggleOff.png').convert_alpha()


# list of windowPads
pads = [{'no':1, 'color': c['lightGreen'], 'text': 'Original', 'icon': imgIcon2},
        {'no':2, 'color': c['lightOrange'], 'text': 'Gray Scale', 'icon': imgIcon3},
        {'no':3, 'color': c['lightPink'], 'text': 'Edges', 'icon': imgIcon4},
        {'no':4, 'color': c['darkPink'], 'text': 'Contours', 'icon': imgIcon5}]



def drawWindowPad(pos, color, text, icon):
    xo, yo, w, h = pos
    # add shadow to the windowpad
    window.blit(imgShadow, (xo-20, yo+h-90))
    # header windowpad
    pygame.draw.rect(window, color, (xo, yo, w, 60), border_top_left_radius=10, border_top_right_radius=10)
    # image area white
    pygame.draw.rect(window, c['white'], (xo, yo+60, w, h-115), border_bottom_left_radius=10, border_bottom_right_radius=10)
    # icon
    window.blit(icon, (xo+15, yo+9))
    # text 
    font = pygame.font.Font('./Resources/Marcellus-Regular.ttf',23)
    text = font.render(text, True, c['darkBrown'])
    window.blit(text, (xo+75,yo+15))



def drawFilterPad():
    drawWindowPad((75, 52, 275, 627), c['darkGreen'], 'Filters', imgIcon1)
    


def drawAll():
    w, h = 275, 301
    gapW, gapH = 72, 25
    drawWindowPad((430, 52, w, h), pads[0]['color'], pads[0]['text'], pads[0]['icon'])
    drawWindowPad((430+gapW+w, 52, w, h), pads[1]['color'], pads[1]['text'], pads[1]['icon'])
    drawWindowPad((430, 52+gapH+h, w, h), pads[2]['color'], pads[2]['text'], pads[2]['icon'])
    drawWindowPad((430+gapW+w, 52+gapH+h, w, h), pads[3]['color'], pads[3]['text'], pads[3]['icon'])

    drawFilterPad()


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

    imgDesign.set_alpha(50)
    # window.blit(imgDesign, (0,0))

    drawAll()

    # update display
    pygame.display.update()

    # set FPS
    clock.tick(fps)

