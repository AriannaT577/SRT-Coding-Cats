import pygame

#COLOURS!
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
PINK = (255, 182, 193)
DARKBLUE = (10, 67, 118)

RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("IntroToGraphics: Nyan Cat")

done = False
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(DARKBLUE)

    # ----- rainbow drawing -----
    pygame.draw.rect(screen, RED, (0, 160, 360, 15))
    pygame.draw.rect(screen, ORANGE, (0, 175, 360, 15))
    pygame.draw.rect(screen, YELLOW, (0, 190, 360, 15))
    pygame.draw.rect(screen, GREEN, (0, 205, 360, 15))
    pygame.draw.rect(screen, BLUE, (0, 220, 360, 15))
    pygame.draw.rect(screen, PURPLE, (0, 235, 360, 15))
    #body
    pygame.draw.rect(screen, PINK, (350, 150, 200, 120))
    pygame.draw.rect(screen, BLACK, (350, 150, 200, 120), 3)
    #ears
    pygame.draw.rect(screen, GRAY, (540, 155, 20, 30))
    pygame.draw.rect(screen, BLACK, (540, 155, 20, 30), 3)
    pygame.draw.rect(screen, GRAY, (610, 155, 20, 30))
    pygame.draw.rect(screen, BLACK, (610, 155, 20, 30), 3)
    #head
    pygame.draw.rect(screen, GRAY, (540, 180, 90, 80))
    pygame.draw.rect(screen, BLACK, (540, 180, 90, 80), 3)
    #eyes
    pygame.draw.circle(screen, BLACK, (565, 210), 5) 
    pygame.draw.circle(screen, BLACK, (605, 210), 5)
    #:3
    pygame.draw.rect(screen, BLACK, (582, 235, 5, 8))
    pygame.draw.arc(screen, BLACK, (570, 230, 30, 15), 3.14, 0, 2)
    #paw
    pygame.draw.rect(screen, GRAY, (360, 260, 25, 25)) 
    pygame.draw.rect(screen, BLACK, (360, 260, 25, 25), 3)
    pygame.draw.rect(screen, GRAY, (390, 260, 25, 25)) 
    pygame.draw.rect(screen, BLACK, (390, 260, 25, 25), 3) 
    pygame.draw.rect(screen, GRAY, (480, 260, 25, 25))  
    pygame.draw.rect(screen, BLACK, (480, 260, 25, 25), 3)
    pygame.draw.rect(screen, GRAY, (510, 260, 25, 25)) 
    pygame.draw.rect(screen, BLACK, (510, 260, 25, 25), 3) 

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
