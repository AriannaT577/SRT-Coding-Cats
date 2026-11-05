from pickle import FALSE
import pygame
import random
from random import randint

from pygame.draw import polygon
 
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE    =(0,0,255)
BLUED    = (   0,   100, 255)
BLUEL    = (   0,   200, 255)
YELLOW   = (255, 255, 0)
BROWN   =  (200, 150, 150)
DBROWN   =  (141, 102, 35)
WINDOWCOLOUR = (   0,   120, 255)
PISSYELLOW = (199,214,84)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("The sigma identifier")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
rect_x = 50
rect_y = 50

rect_change_x = 5
rect_change_y = 5

rect_B = 50

poly_x = 350
poly_y = 200

poly_change_x = 5
poly_change_y = 4
poly_change_y2 = 10

poly_x2 = 150
poly_y2 = 200

poly_y3 = 30



# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here

    if rect_y > 450 or rect_y < 0:
        rect_change_y = rect_change_y * -1
    if rect_x > 650 or rect_x < 0:
       rect_change_x = rect_change_x * -1
    if rect_x > 650 or rect_x < 0:
        rect_B += 2
    if rect_y > 450 or rect_y < 0:
        rect_B += 2
    if rect_x > 649:
        rect_change_x = rect_change_x + 5
        rect_change_x = rect_change_x * -1
    if rect_x < 1:
        rect_change_x = rect_change_x - 5
        rect_change_x = rect_change_x * -1


    if poly_y > 450 or poly_y < 0:
        poly_change_y = poly_change_y * -1
    if poly_x > 650 or poly_x < 0:
       poly_change_x = poly_change_x * -1

    if poly_y3 > 450 or poly_y3 < 0:
       poly_change_y2 = poly_change_y2 * -1


   

    #if poly_y2 > 450 or poly_y2 < 0:
    #    poly_change_y = poly_change_y * -1
    #if poly_x2 > 650 or poly_x2 < 0:
    #   poly_change_x = poly_change_x * -1
   
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLUEL)
 
    # --- Drawing code should go here
    pygame.draw.rect(screen,GREEN,[0,300,700,200],0)

    pygame.draw.rect(screen,BROWN,[25,150,150,150])
    pygame.draw.polygon(screen,BLACK,((25,150),(175,150),(100,100)))
    pygame.draw.circle(screen,WINDOWCOLOUR,(100,215),20)
    pygame.draw.rect(screen,DBROWN,[150,250,25,50])#build the scene
   
   
    pygame.draw.rect(screen, BLUE, [rect_x, rect_y, rect_B, rect_B]) #bouncing squares
    rect_x += rect_change_x
    rect_y += rect_change_y
    pygame.draw.polygon(screen, PISSYELLOW, [(int(poly_x),int(poly_y)),(int(poly_x2),int(poly_y3)),(250,int(poly_y2))]) #bouncing polygon
    poly_x += poly_change_x
    poly_y += poly_change_y
    poly_x2 += poly_change_x
    poly_y2 += poly_change_y
    poly_y3 += poly_change_y2

    font = pygame.font.SysFont('Calibri', 25, True, False) #You are not sigma
    text = font.render("You are not Sigma",False, RED)
    DREAM = font.render("This Is a DREAM",False, BLACK)

    screen.blit(text, [250, 250])#place the sigma identifier
    screen.blit(DREAM, [50, 300])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()