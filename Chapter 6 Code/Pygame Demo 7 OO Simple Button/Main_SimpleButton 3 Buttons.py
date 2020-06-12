#  Pygame demo 7 3-Button Test

# 1 - Import packages
import pygame
from pygame.locals import *
from SimpleButton import *
import sys

# Define constants
GRAY = (200, 200, 200)
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 100
FRAMES_PER_SECOND = 30 

# 2 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  

# 4 - Load assets: image(s), sounds, etc.

# 5 - Initialize variables
# Create instances of SimpleButton
oButtonA = SimpleButton(window, (25, 30), \
                        'images/buttonAUp.png', \
                        'images/buttonADown.png')
oButtonB = SimpleButton(window, (150, 30), \
                        'images/buttonBUp.png', \
                        'images/buttonBDown.png')
oButtonC = SimpleButton(window, (275, 30), \
                        'images/buttonCUp.png', \
                        'images/buttonCDown.png')

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            sys.exit()

        # Pass the event to each button, see if oned has been clicked on
        if oButtonA.handleEvent(event):
            print('User clicked button A.')
        elif oButtonB.handleEvent(event):
            print('User clicked button B.')
        elif oButtonC.handleEvent(event):
            print('User clicked button C.')


    # 8 - Do any "per frame" actions
    
    # 9 - Clear the screen
    window.fill(GRAY)
    
    # 10 - Draw all screen elements
    oButtonA.draw()
    oButtonB.draw()
    oButtonC.draw()

    # 11 - Update the screen
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait the correct amount
